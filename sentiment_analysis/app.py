from datetime import datetime
import requests
from sqlite3 import Timestamp
from time import time
from flask import Flask, request, render_template
from transformers import BertModel, BertTokenizer, AdamW
import torch
# from database import Database

from elasticsearch import Elasticsearch, helpers

es = Elasticsearch(f"http://elasticsearch:9200")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle

from torch import nn, optim
import tweepy


# database = Database()


RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class_names = ['negative', 'neutral', 'positive']
PRE_TRAINED_MODEL_NAME = 'bert-base-cased'
tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)
MAX_LEN = 280

class SentimentClassifier(nn.Module):
  def __init__(self, n_classes):
    super(SentimentClassifier, self).__init__()
    self.bert = BertModel.from_pretrained(PRE_TRAINED_MODEL_NAME, return_dict=False)
    self.drop = nn.Dropout(p=0.3)
    self.out = nn.Linear(self.bert.config.hidden_size, n_classes)
  
  def forward(self, input_ids, attention_mask):
    _, pooled_output = self.bert(
      input_ids=input_ids,
      attention_mask=attention_mask
    )
    output = self.drop(pooled_output)
    return self.out(output)

model = SentimentClassifier(len(class_names))
model.load_state_dict(torch.load('best_model_state_e10.bin', map_location=torch.device('cpu')))
model = model.to(device)

# predict sentiments
def pred(inpText):
  encoded_review = tokenizer.encode_plus(
  inpText,
  max_length=MAX_LEN,
  add_special_tokens=True,
  return_token_type_ids=False,
  pad_to_max_length=True,
  return_attention_mask=True,
  return_tensors='pt',
  )
  input_ids = encoded_review['input_ids'].to(device)
  attention_mask = encoded_review['attention_mask'].to(device)

  output = model(input_ids, attention_mask)
  _, prediction = torch.max(output, dim=1)
  return class_names[prediction]

# add data to elasticsearch
def es_bulk_doc(data, index: str):
          for document in data:
              yield {
                  "_index": index,
                  "_source": document
              }


# your bearer token
MY_BEARER_TOKEN = "xxxxxx"
# create your client 
client = tweepy.Client(bearer_token=MY_BEARER_TOKEN)

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def predict():
    if request.method == "POST":
        hashtag = request.form['tag']
        start_time = request.form['start']
        end_time = request.form['end']
        max_results = int(request.form['max'])
        
        tweets = client.search_recent_tweets(query=hashtag + " lang:en -is:retweet",
                                            start_time=start_time,
                                            end_time=end_time,
                                            tweet_fields = ["text", "created_at"],
                                            max_results = max_results
                                            )


        tweet_info_ls = []

        for tweet in tweets.data:
            tweet_info = {
                'Tweet': tweet.text,
                'Created_at': tweet.created_at,
                'Sentiment': pred(tweet.text)
            }
            tweet_info_ls.append(tweet_info)
        
        tweets_df = pd.DataFrame(tweet_info_ls)
        # tweets_df['Sentiment']=tweets_df['Tweet'].apply(pred)
        tweets_df['Hashtag']= hashtag

        # data -> list of dictionaries
        data = tweets_df.to_dict(orient='records')
        helpers.bulk(es, es_bulk_doc(data, index='tweet'))
        return render_template('index.html', data=data)
    else:
        return render_template('index.html', error_message="Enter some hashtag!")


@app.route('/news', methods = ['POST', 'GET'])
def news():
    if request.method == "POST":
        hashtag = request.form['tag']
        start_time = request.form['start']
        end_time = request.form['end']
        
        url = ('https://newsapi.org/v2/everything?q=' + hashtag + '&from=' + start_time + '&to=' + end_time + '&sortBy=popularity&apiKey=34c1c3ee346c45d2a82088d58245b74c')
        response = requests.get(url)
        data = response.json()

        df = {"Keyword": [], "Post": [], "Created_at": [], "Source": [], "Sentiment": []}
        for i in range(len(data['articles'])):
          Post = data['articles'][i]['content']
          Created_at = data['articles'][i]['publishedAt']
          Source = data['articles'][i]['source']['name']
          Sentiment = pred(Post)

          df["Keyword"].append(hashtag)
          df["Post"].append(Post)
          df["Created_at"].append(Created_at)
          df["Source"].append(Source)
          df["Sentiment"].append(Sentiment)
          

        df = pd.DataFrame(df)
        data = df.to_dict(orient='records')
        helpers.bulk(es, es_bulk_doc(data, index='news'))
        return render_template('news.html', data=data)
    else:
        return render_template('news.html', error_message="Enter some hashtag!")




if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=5000)

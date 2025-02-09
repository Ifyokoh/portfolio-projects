# **Real-Time Sentiment Analysis**  
_Analyze public sentiment in real-time using BERT, Flask, Docker, Elasticsearch, and Kibana._  

## **Project Overview**  
This project is a real-time Twitter Sentiment Analysis tool with a Flask-based frontend, allowing users to enter a hashtag and date range to analyze sentiment trends over time. Using BERT for NLP, the system classifies tweets into positive, negative, or neutral sentiments. The processed data is stored in Elasticsearch, enabling efficient searching and filtering. Kibana is then used to visualize trends and insights through interactive dashboard, making it easy to explore how people feel about a topic over time, such as a product or event. The project can be extended to integrate data from News APIs and Facebook, expanding its capabilities for broader sentiment analysis.  

The goal is to help businesses track public opinion, improve customer engagement, and make data-driven decisions.    

---

## **How to Run This Project**
### **Clone the Repository**
```bash
git clone https://github.com/Ifyokoh/portfolio-projects.git
cd portfolio-projects/sentiment_analysis
```

### **Set Up Environment Variables**
Create a `.env` file and add your Twitter API credentials:
```
TWITTER_CONSUMER_KEY=your_api_key
TWITTER_CONSUMER_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_secret
```

### **Start the Docker Containers**
```bash
docker-compose up -d
```
This will start up Flask API, Elasticsearch database and Kibana dashboard  

### **Access the Dashboard**
**Kibana UI:** [http://localhost:5601](http://localhost:5601)  
**Flask API:** [http://localhost:5000](http://localhost:5000)  

---

## **Project Structure**
```
sentiment_analysis/
|- template/
| |- index.html              # main page/twitter page of web app
| |- news.html              # news page of web app
| |- results.html            # classification result page of web app
│── app.py                   # Flask API for sentiment analysis
|── dockerfile               # Dockerfile for app setup
│── docker-compose.yml       # Docker configuration
│── requirements.txt         # Python dependencies
```

---

## **Key Features**
- Real-Time Sentiment Analysis – Monitors public opinion live  
- Deep Learning-Based Classification – Uses BERT model for high accuracy  
- Scalable & Containerized – Deployed with Docker
- Fast Data Storage & Retrieval – Uses Elasticsearch  
- Interactive Data Visualization – Insights via Kibana Dashboard
 


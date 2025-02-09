# **Fine-Tuning a Generative AI Model**  
_Training a custom AI model to classify news articles as positive or negative using a self-built dataset._  

## **Project Overview**  
This project involves fine-tuning a pretrained transformer language model AfriBERTa to classify news articles based on sentiment in the Igbo language. I scraped news topics from the BBC website and manually annotated them with positive or negative sentiment. The model is trained to understand context and tone in news reporting, making it useful for media monitoring and sentiment tracking. 

This approach can be adapted for domain-specific tasks such as analyzing customer feedback. By fine-tuning a language model on specialized datasets, it can be leveraged for targeted applications in business.    

---

## **Key Features**  
- Custom Dataset – Created from real-world news articles 
- Web Scraping & Data Annotation – data collection by scraping using BeautifulSoup & Requests
- Data Preprocessing and analysis using python and pandas 
- Fine-Tuned AI Model – Tailored for sentiment analysis using Pytorch  
- The manually annotated [dataset](Ifyokoh/IgboSenti-BBC) and The trained [model](Ifyokoh/Igbo-sentiment-bbc) can be loaded directly from the Hugging Face 




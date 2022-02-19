from flask import Flask
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="9713667a7fb34b9b9d9848b3e4d19379")
    
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")
    
    articles = topheadlines('articles')
    
    desc = []
    nes=[]
    img=[]
    
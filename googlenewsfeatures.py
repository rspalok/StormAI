import requests
import json
import pprint


def getgooglenews(no_of_news):
    response_news=requests.get('https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=eb3eb4733fe1443983b704252b928eaf')
    news_list = []
    for news in range(no_of_news) :
        news_list.append(response_news.json().get('articles')[news].get('description'))

    #print(news_list)
    return news_list
import requests



def getgooglenews(no_of_news,region):
    if region == 'india' or region == 'local' or region == 'indian':
        response_news = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=eb3eb4733fe1443983b704252b928eaf')
        news_list = []
        for news in range(no_of_news):
            news_list.append(response_news.json().get('articles')[news].get('description'))
        return news_list

    else:
        response_news=requests.get('https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=eb3eb4733fe1443983b704252b928eaf')
        news_list = []
        for news in range(no_of_news) :
            news_list.append(response_news.json().get('articles')[news].get('description'))
    return news_list
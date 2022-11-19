import newsapi
import os
import json
import apk.py

apikey = apk.apiKey


nsap = newsapi.NewsApiClient(api_key=apiKey)

articles = nsap.get_top_headlines(country='in',category='entertainment',page_size=25)

article = arrticles['articles']
author = []
title = []
img = []
for i in range(len(article)):
    auth = artic[i]
    author.append(auth['author'])
    title.append(auth['title'])
    img.append(auth['urlToImage'])

values = zip(author,title,img)






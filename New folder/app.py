from flask import *
import os
import newsapi
import apk

app = Flask(__name__)

apikey = apk.apiKey

@app.route('/')
@app.route('/home')
def home():
    nsap = newsapi.NewsApiClient(api_key=apikey)
    articles = nsap.get_top_headlines(country='in',page_size=25)
    article = articles['articles']
    author = []
    title = []
    img = []
    for i in range(len(article)):
        auth = article[i]
        author.append(auth['author'])
        title.append(auth['title'])
        img.append(auth['urlToImage'])
        values = zip(author,title,img)
    return render_template('home.html',value= values)

@app.route('/technology')
def technology():
    nsap = newsapi.NewsApiClient(api_key=apikey)
    articles = nsap.get_top_headlines(country='in',category='technology',page_size=25)
    article = articles['articles']
    author = []
    title = []
    img = []
    for i in range(len(article)):
        auth = article[i]
        author.append(auth['author'])
        title.append(auth['title'])
        img.append(auth['urlToImage'])
        values = zip(author,title,img)
    return render_template('tech.html',value= values)

@app.route('/business')
def business():
    nsap = newsapi.NewsApiClient(api_key=apikey)
    articles = nsap.get_top_headlines(country='in',category='business',page_size=25)
    article = articles['articles']
    author = []
    title = []
    img = []
    for i in range(len(article)):
        auth = article[i]
        author.append(auth['author'])
        title.append(auth['title'])
        img.append(auth['urlToImage'])
        values = zip(author,title,img)
    return render_template('business.html',value= values)

@app.route('/sports')
def sports():
    nsap = newsapi.NewsApiClient(api_key=apikey)
    articles = nsap.get_top_headlines(country='in',category='sports',page_size=25)
    article = articles['articles']
    author = []
    title = []
    img = []
    for i in range(len(article)):
        auth = article[i]
        author.append(auth['author'])
        title.append(auth['title'])
        img.append(auth['urlToImage'])
        values = zip(author,title,img)
    return render_template('sports.html',value= values)


if __name__=='__main__':
    app.run(debug=True)

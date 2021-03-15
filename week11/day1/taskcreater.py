from flask import Flask, render_template
import random
from requests import get








url = "https://newsapi.org/v2/everything"
token = "5719809a4f814d0d9f8cb98e7a3d97de"

def get_news(query):
    querry = query
    params = {
        "apiKey": token,
        "q": querry,
        "from": "2021-03-01"
    }
    
    results = get(url, params=params)
    author = results.json()['articles'][0]['author']
    title = results.json()['articles'][0]['title']
    description = results.json()['articles'][0]['description']
    # return f" <h1> {title} </h1> <br> <p> {description} </p> <br> <p> {author} </p> "

# print(get_news("news"))




def get_news_normal(query):
    params = {
        "apiKey": token,
        "q": "query",
        "from": "2021-03-01"
    }

    results = get(url, params=params)
    return results.json()['articles']

# print(get_news("python"))











app = Flask(__name__)


@app.route('/')
def index_off():
    return f'<h1> Hello Hello </h1>'
@app.route('/home')
def homepage():
    return "<html><body><h3> Hello world ! </h3></body></html>"

# @app.route('/name/files')
# def page1():
#     return render_template("index.html")


@app.route('/news/<name>')
def say_hello(name):
    url = "https://newsapi.org/v2/everything"
    token = "5719809a4f814d0d9f8cb98e7a3d97de"
    name1 = name

    params = {
        "apiKey": token,
        "q": name1,
        "from": "2021-03-01"
    }

    results = get(url, params=params)
    new_number = random.randint(0,20)
    new = get_news(name1)
    author = results.json()['articles'][new_number]['author']
    title = results.json()['articles'][new_number]['title']
    description = results.json()['articles'][new_number]['description']
    return render_template('greet.html', name= name, author=author, title = title, description = description, results = results)


# @app.route('/age/<age>')
# def can_buy_alcohol(age):
#     if int(age) < 18:
#         return f"you have {str(age)} years old, canot sell you alcohol"
#     elif int(age) == 18:
#         return f"welcome yo your firs year of drinking"
#     else:
#         return f'welcome, wath you want to buy'



# @app.route(f'/random_number')
# def page_number():
#     number = random.randint(0,100) 
#     return str(number)

# @app.route('/blog')
# def say_hello2(name):
#     return f"<h1> welcome to my blog </h1>"



# @app.route('/article/<name>')
# def say_hello2(name):
#     return f"<h1> welcome to my blog </h1>"








app.run(port=5001)
from flask import Flask
import random
from requests import get








url = "https://newsapi.org/v2/everything"
token = "5719809a4f814d0d9f8cb98e7a3d97de"

def get_news(query):
    params = {
        "apiKey": token,
        "q": "query",
        "from": "2021-03-01"
    }

    results = get(url, params=params)
    return results.json()['articles']

print(get_news("python"))














app = Flask(__name__)


@app.route('/')
def index_off():
    return f'<h1> Hello Hello </h1>'
@app.route('/home')
def homepage():
    return "<html><body><h3> Hello world ! </h3></body></html>"


@app.route('/hi/<name>')
def say_hello(name):
    return f"Hello {name} Nice to meet you"


@app.route('/age/<age>')
def can_buy_alcohol(age):
    if int(age) < 18:
        return f"you have {str(age)} years old, canot sell you alcohol"
    elif int(age) == 18:
        return f"welcome yo your firs year of drinking"
    else:
        return f'welcome, wath you want to buy'



@app.route(f'/random_number')
def page_number():
    number = random.randint(0,100) 
    return str(number)

@app.route('/blog')
def say_hello2(name):
    return f"<h1> welcome to my blog </h1>"



@app.route('/article/<name>')
def say_hello2(name):
    return f"<h1> welcome to my blog </h1>"








# app.run(port=5001)
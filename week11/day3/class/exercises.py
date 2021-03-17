import flask
import random
from datetime import datetime
from requests import get     # "Module not found" --> pip install requests

# url = "https://newsapi.org/v2/everything"
# token = "5719809a4f814d0d9f8cb98e7a3d97de"

# def get_news(query):
#     params = {
#         "apiKey": token,
#         "q": "query",
#         "from": "2021-03-01"
#     }

#     results = get(url, params=params)
#     return results.json()['articles']
today = datetime.now()
# print(today)
# Create a controller using flask.Flask class
app = flask.Flask(__name__)     # __name__ is the name of the file

# Create one route: a function that is assigned to a URL
# 127.0.0.1:5000/ <--> route "/"
# 127.0.0.1:5000/home <--> route "/home"
@app.route("/datetime")
def datetime():
    
    year = today.year
    month = today.month
    day = today.day
    hour = today.hour
    minute = today.minute
    second = today.second

    return flask.render_template('datetoday.html', year = year, month = month, day = day, hour = hour, minute = minute, second = second)

@app.route("/home") # --> Will assign the function to www.yourdomain.com/home
def homepage():
    return "<html><body><h3> Hello world ! </h3></body></html>"

# Create a function so that when a user calls
# 127.0.0.1:5000/random-nu@app.route("/")

# He sees a random number between 1 and 100 on his screen
@app.route("/random-number")
def random_number():
    number = random.randint(1, 100)
    return f"Your number is: {number}"

# 127.0.0.1:5000/greet/eyal --> Hello, eyal, nice to see you
# 127.0.0.1:5000/greet/rick

# @app.route("/greet/<name>")
# def greeting_message(name):
#     # Create a template: greet.html
#     # Add an h1 tag that says hello to the user (using his name)
#     return flask.render_template("greet.html", name=name)

# @app.route('/news/<topic>')
# def news(topic):
#     articles = get_news(topic)[:5]

#     return flask.render_template("articles.html", articles=articles)



# Run the application server
app.run(port=5001, debug=True)




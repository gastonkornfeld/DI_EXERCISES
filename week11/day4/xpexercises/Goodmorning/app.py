
# Exercise 1 : Good Morning
# Instructions :
# Create a view that displays a greeting message.
#  The greeting message should change depending on the time of day the url to this view is accessed.

import datetime

from flask import Flask, render_template, request

today = datetime.datetime.now()
today_hour_of_the_day = today.hour

# print(today_hour_of_the_day)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", hour=today_hour_of_the_day)

app.run(debug=True)

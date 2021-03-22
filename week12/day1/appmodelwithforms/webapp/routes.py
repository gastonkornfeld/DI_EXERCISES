import flask

from . import app       # . is webapp/
from . import forms, news_functions

@app.route("/")
def home():
    return "Hello world !"

@app.route('/test-form', methods=["GET", "POST"])
def test():
    # Create an instance of the form
    form = forms.TestForm()
    if flask.request.method == "POST":
        print('name', form.name.data)
        print("age", form.age.data)

    return flask.render_template("test_form.html", form=form)




@app.route('/login', methods=["GET", "POST"])
def login():
    # Create an instance of the form
    form1 = forms.FullForm()
    if flask.request.method == "POST":
        articles = news_functions.get_news(form1.query.data)

        return flask.render_template('search.html', articles = articles)
        

    return flask.render_template("login.html", form1=form1)
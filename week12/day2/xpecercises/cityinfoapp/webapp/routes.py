import flask
import json

from . import app       
from . import forms


@app.route("/")
@app.route("/home")
def home():
    return "go to add_city for the app."


@app.route('/about')
def about():
    return flask.render_template('about.html', title = 'About')







@app.route('/add_city',  methods=['GET', "POST"])
def add_city():
    
    
    form = forms.AddCityForm()
    
    if form.validate_on_submit():
        flask.flash("You add the city!", 'success')
        with open('city_list.json', 'a') as f:
            json.dump(flask.request.form, f)
        return flask.render_template('new_city.html', form = form)
    else:
        return flask.render_template('add_city.html', title = 'ADD CITY', form = form)

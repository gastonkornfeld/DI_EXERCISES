import flask

from . import app, funct
from . import models
from . import forms
from . import db


@app.route("/")
@app.route("/home")
def home():
    return flask.render_template('home.html')


@app.route('/users')
def users():
    all_users =  models.User.query.all()
    roscoview = models.User.query.filter_by(city='Roscoeview')
    return flask.render_template('users.html', all_users = all_users, ros = roscoview)


@app.route('/id_profile/<int:id_user>')
def profile(id_user):
    user =  models.User.query.get(id_user)
    return flask.render_template('profile.html', user = user)


@app.route('/add_user', methods=['GET', "POST"])
def add_user():
    form = forms.AddUserForm()
    if form.validate_on_submit():
        username = form.username.data
        street = form.street.data
        city = form.city.data
        zipcode = form.zipcode.data
        new_user = models.User(name = username, street = street, city = city, zip_code = zipcode)
        db.session.add(new_user)
        db.session.commit()
        flask.flash(f'Username added Succesfully', 'success')

        return flask.redirect(flask.url_for('users'))
    return flask.render_template('add_user.html', title = 'ADD user', form = form)



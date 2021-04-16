
import flask
from faker import Faker
from . import app       
from . import models
from . import forms
from . import db


fake = Faker()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.PersonForm()
    if form.validate_on_submit():
        phone = form.phone.data
        email = form.email.data
        address = form.address.data
        name = form.name.data


        return flask.redirect(flask.url_for('show_phone'))
    return flask.render_template('index.html', form=form)



@app.route('/showphone')
def show_phone():
    all_persons = models.Person.query.all()
    return flask.render_template('show_phone.html', persons = all_persons)


@app.route('/person/<phone_number>')
def show_by_phone(phone_number):
    fake = Faker()
    number = models.Phonenumber(number = phone_number)
    person = models.Person(name = fake.name(), email = fake.email(), phone_numbers= [number], address = fake.address())
    return flask.render_template('by_number.html', person = person)


@app.route('/person1/<person_name>')
def show_by_name(person_name):
    fake = Faker()
    number = models.Phonenumber(number = fake.phone_number())
    person = models.Person(name = person_name, email = fake.email(), phone_numbers= [number], address = fake.address())
    return flask.render_template('by_number.html', person = person)




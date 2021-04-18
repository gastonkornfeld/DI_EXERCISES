
import flask
from faker import Faker
from . import app       
from . import models
from . import forms
from . import db
from random import randint


fake = Faker()
# route used to fill the database, it was not adding the persons in to the nationalities
# so only argentina and afganistan that i add mannualy are working


@app.route('/test')
def test():
    first = models.Person.query.get(3)
    natio = models.Nationality.query.get(3)
    first.nationalities.append(natio)
    natio.persons.append(first)
    db.session.commit()

#     fake = Faker()
#     for i in range(500):

    
#         nationality = models.Nationality(name = fake.country())
#         number = models.Phonenumber(number = fake.phone_number()) #get the number inserted in the url
#         person = models.Person(name = fake.name(), email = fake.email(), phone_numbers= [number], address = fake.address(), nationalities = [nationality])
#         db.session.add(person) # create a person with this number and this nationality
        
#         db.session.commit()
    return flask.redirect(flask.url_for('all_data'))





@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.PersonForm()
    if form.validate_on_submit():
        phone = models.Phonenumber(number = form.phone.data)
        email = form.email.data
        address = form.address.data
        name = form.name.data
        if models.Nationality.query.filter_by(name = form.nationality.data).first() == None:
            nationality = models.Nationality(name = form.nationality.data)
            person = models.Person(name = name, email = email, phone_numbers= [phone], address = address, nationalities = [nationality])
            db.session.add(person)
            db.session.commit()
            flask.flash('Added to the database', 'success')
            return flask.redirect('/person1/' + name)
        else:
            nationality = models.Nationality.query.filter_by(name = form.nationality.data).first()
            person = models.Person(name = name, email = email, phone_numbers= [phone], address = address, nationalities = [nationality])
            
            db.session.add(person)
            nationality.persons.append(person)
            db.session.commit()
            flask.flash('Added to the database', 'success')
            return flask.redirect('/person1/' + name)
    return flask.render_template('index.html', form=form)



@app.route('/all_data')
def all_data():
    all_persons = models.Person.query.all()
    return flask.render_template('all_data.html', persons = all_persons)


@app.route('/search_number', methods=['GET', 'POST'])
def search_number():
    form = forms.Search_numberForm()
    if form.validate_on_submit():
        number = form.number.data
        return flask.redirect('/person/' + number)
    return flask.render_template('search_number.html', form=form)



@app.route('/person/<phone_number>')
def show_by_phone(phone_number):
    number1 = models.Phonenumber.query.filter_by(number = phone_number ).first()
    if number1 != None:
        person = models.Person.query.get(number1.owner)
        return flask.render_template('by_number.html', person = person, number = phone_number)
    return flask.render_template('by_number.html', person = None)




@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    form = forms.Search_nameForm()
    if form.validate_on_submit():
        name = form.name.data
        return flask.redirect('/person1/' + name)
    return flask.render_template('search_name.html', form=form)


@app.route('/person1/<person_name>')
def show_by_name(person_name):
    person = models.Person.query.filter_by(name=person_name).first()
    return flask.render_template('by_name.html', person = person)


@app.route('/search_nationality', methods=['GET', 'POST'])
def search_nationality():
    form = forms.Search_nationalityForm()
    if form.validate_on_submit():
        nationality = form.nationality.data
        return flask.redirect('/people/' + nationality)
    return flask.render_template('search_nationality.html', form=form)



@app.route('/people/<nationality>')
def show_by_nationality(nationality):
    nationality_persons = models.Nationality.query.filter_by(name = nationality).first()
    flask.flash("search finished", 'success')

    return flask.render_template('by_nationality.html', person = nationality_persons)


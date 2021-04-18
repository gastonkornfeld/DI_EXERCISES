
from . import db


nationality_table = db.Table('nationalities',
                      db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
                      db.Column('nationality_id', db.Integer, db.ForeignKey('nationality.id'))
)

class Person(db.Model):
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(124), unique = True)
    phone_numbers = db.relationship('Phonenumber', backref= 'person', lazy='dynamic')
    address = db.Column(db.String(124))
    nationalities = db.relationship("Nationality", secondary = nationality_table, back_populates="persons")
    

class Phonenumber(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    number = db.Column(db.String(128), unique = True)
    owner = db.Column(db.Integer, db.ForeignKey('person.id'))

class Nationality(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128))
    persons = db.relationship("Person", secondary = nationality_table, back_populates="nationalities")
   
   

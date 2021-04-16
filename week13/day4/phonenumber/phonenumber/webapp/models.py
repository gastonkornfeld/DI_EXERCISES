
from . import db
class Person(db.Model):
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(124), unique = True)
    phone_numbers = db.relationship('Phonenumber', backref= 'person')
    address = db.Column(db.String(124))
    

class Phonenumber(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    number = db.Column(db.String(128), unique = True)
    owner = db.Column(db.Integer, db.ForeignKey('person.id'))



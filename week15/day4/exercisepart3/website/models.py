from . import db

from flask_login import UserMixin
from sqlalchemy.sql import func

# importin the mixin and adding to the user model make our user be able to use the flask login 



available_table = db.Table('available_in',
                      db.Column('film_id', db.Integer, db.ForeignKey('film.id')),
                      db.Column('country_id', db.Integer, db.ForeignKey('country.id'))
)


category_table = db.Table('categories',
                      db.Column('film_id', db.Integer, db.ForeignKey('film.id')),
                      db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)

director_table = db.Table('directors',
                      db.Column('film_id', db.Integer, db.ForeignKey('film.id')),
                      db.Column('director_id', db.Integer, db.ForeignKey('director.id'))
)




class Country(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    movies_created = db.relationship('Film', backref= 'country', lazy='dynamic')
    films_availables = db.relationship("Film", secondary = available_table, back_populates="available_in")
 
    def create_country(country_name):
        return Country(name = country_name)


class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    films_in = db.relationship('Film', secondary = category_table, back_populates='categories')

    

class Film(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    created_in = db.Column(db.Integer(), db.ForeignKey('country.id'))
    available_in = db.relationship("Country", secondary = available_table, back_populates="films_availables")
    categories = db.relationship('Category', secondary = category_table, back_populates='films_in') #many to many
    directors = db.relationship('Director', secondary = director_table, back_populates='films_directed')
    
    
  

class Director(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    films_directed = db.relationship('Film', secondary = director_table, back_populates='directors')


    


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    name = db.Column(db.String(150))
    status = db.Column(db.String(150))
    






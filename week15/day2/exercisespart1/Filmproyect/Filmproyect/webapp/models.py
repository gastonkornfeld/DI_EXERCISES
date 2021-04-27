from . import db



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

    def create_category(category_name):
        return Category(name = category_name)


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


    def create_director(name, last_name):
        return Director(first_name = name, last_name = last_name)



    # def add_film(director_id, film_to_add_to_director):
    #     """
    #         given a director id and a film is gonna be added to the list of films of the director
    #     """
    #     director = Director.query.get(director_id)
    #     director.films_directed.append(film_to_add_to_director)
    #     film_to_add_to_director.directors.append(director)
        
    #     return None
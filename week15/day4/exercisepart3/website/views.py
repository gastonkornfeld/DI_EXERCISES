
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from . import models, forms
from . import db
import json

views = Blueprint('views', __name__)






@views.route("/")
@login_required
def home():
    # movie = models.Film.query.get(5)
    # db.session.delete(movie)
    # db.session.commit()
    

    return render_template('homepage.html', user = current_user)


@views.route("/movies")
@login_required
def movies():
    directors = models.Director.query.all()
    films = models.Film.query.all()
    countries = [] #will create a variable to retrieve the countryes information that is just getting a number
    for film in films:
        countries.append(models.Country.query.get(film.created_in)) # get all the categories in the list
    categories = models.Category.query.all()
    lenght = len(list(films)) # need this variable to make a range loop for the movies in the render
    
    return render_template('movies.html', films = films, countries = countries, leng = lenght, user=current_user)


@views.route("/info")
@login_required
def info():
    directors = models.Director.query.all()
    films = models.Film.query.all()
    countries = models.Country.query.all()
    categories = models.Category.query.all()
    return render_template('info.html' ,directors = directors, films= films, countries = countries, user=current_user)

@views.route('/addfilm', methods = ['GET', 'POST'])
@login_required
def addFilm():
    # retrieve the data from the form
    form = forms.AddFilmForm()
    films = models.Film.query.all()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.name.data
            year = form.year.data
            country = form.created_in.data
            # with the categories i want to retrieve the different categories in a list and then
            # chek if they exis if they not create them and then in the end use the categories to the film.
            categories = form.categories.data.split(',')
            # withthe director also check if exist to create it if not continue
            director = form.director.data.split(',')
            if len(director) == 2:
                dname = director[0]
                dlast_name = director[1]
                if models.Director.query.filter_by(first_name = dname, last_name = dlast_name).first() == None:
                    new_Director = models.Director(first_name = dname, last_name = dlast_name)
                    db.session.add(new_Director)
            else:
                flash('You need to put the director name followed by "," and the last name', 'danger')
                return redirect(url_for('addFilm'))
            for category in categories:
                if models.Category.query.filter_by(name = category).first() == None:
                    new_category = models.Category(name = category) #cheking that every category is not created
                    db.session.add(new_category)
                    db.session.commit()
        # now that i know all the categories exist i can added to the film
            # if the country already exist in the database i use it if not i need to create it
            if models.Country.query.filter_by(name = country).first() == None:
                new_country = models.Country(name = country)
                db.session.add(new_country)
                db.session.commit()

            # retrieve the existing country and added in to the film creation
            country = models.Country.query.filter_by(name = country).first()
            # create the new film with the info, add the film to the country list of films created
            new_film = models.Film(title = title, year = year)
            db.session.add(new_film)
            country.movies_created.append(new_film)
            # add also the director in to the movie and the movie in to the director
            dname = director[0]
            dlast_name = director[1]
            director = models.Director.query.filter_by(first_name = dname, last_name = dlast_name).first()
            new_film.directors.append(director)
            director.films_directed.append(new_film)
            for category in categories:
                category = models.Category.query.filter_by(name = category).first() #take each category
                category.films_in.append(new_film) #put it in the categories film list
                new_film.categories.append(category) #add the category to the film
            db.session.commit()
            flash('Film Added to the database', 'success')
            return redirect(url_for('views.addFilm'))
    

    return render_template('addfilm.html', form = form, films = films, user=current_user)

@views.route('/add_director', methods = ['GET', 'POST'])
@login_required
def add_director():
    form = forms.AddDirectorForm()
    directors = models.Director.query.all()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            last_name = form.last_name.data
            
            # if the director already exist in the database i use it if not i need to create it
            if models.Director.query.filter_by(first_name = name, last_name = last_name).first() == None:
                new_Director = models.Director(first_name = name, last_name = last_name)
                db.session.add(new_Director)
                # add the film now
                db.session.commit()
                return redirect(url_for('views.add_director'))
            else:
                # tell the user the director already exist in the database
                flash('Director already founded in database', 'info')
                return redirect(url_for('views.add_director'))
    
    return render_template('add_director.html', form = form, directors = directors, user=current_user)







@views.route("/profile")
@login_required
def profile():
    
    

    return render_template('profile.html', user = current_user)

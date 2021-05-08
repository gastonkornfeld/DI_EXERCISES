from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User, Deckofcards
# this two ones are for secure the password
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, forms
from flask_login import login_user, login_required, logout_user, current_user
import random


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            # this is the line that checks if the password match the hash built in
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', 'success')
                session['id_user_logged'] = str(user.id)
                
                # login_user(user, remember=True) #log in the user
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', 'danger')
        else:
            flash('Email does not exist.', 'danger')

    return render_template("login.html", form = form)


@auth.route('/logout')
# @login_required
def logout():
    session['id_user_logged'] = 0
    # logout_user()
    flash('log out succesfully', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = forms.SignUpForm()
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        name = request.form.get('name')
        status1 = random.choice(['admin', 'user', 'user'])
        url = request.form.get('image_url')
        prof_type = random.choice(['Robot', 'Human', 'Monster', 'Pizza Delivery', 'Alien'])
        

        user = User.query.filter_by(email=email).first()
        # all of this is only to show personalize messages to the user when sign up
        if user:
            flash('Email already exists.', 'danger')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', 'danger')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', 'danger')
        elif password1 != password2:
            flash('Passwords don\'t match.', 'danger')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', 'danger')
        else:
            # create the user in the database
            # note the password was generate using the generate password hash
            
            
            new_user1 = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'), name = name, status = status1, prof_type = prof_type, points = 0, image_url = url, have_deck = 'no', coins = 125000)
            db.session.add(new_user1)
            db.session.commit()

            # after sign up, log in the user and the rememeber is to keep the log in 
            # login_user(new_user1, remember=True)
            flash('Account created!', 'success')
            session['id_user_logged'] = str(new_user1.id)
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", form = form)
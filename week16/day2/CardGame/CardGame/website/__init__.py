from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user
from flask_mail import Mail

# init database
db = SQLAlchemy()
DB_NAME = "futuapi.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # need to import my models for the app
    from .models import User, Deckofcards, Futucard, Message, Thread, Transaction

    create_database(app)
    mail_manager = Mail()
    login_manager = LoginManager()
    # this line set the redirect to this page if there is a log in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    mail_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        if id.isdigit():


            return User.query.get(int(id))

    return app

# this part create the database if doesnt exist the path
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
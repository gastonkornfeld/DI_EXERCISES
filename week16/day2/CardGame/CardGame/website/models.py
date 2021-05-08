from . import db
import datetime
import random
from . import apifile
from flask_login import UserMixin
from sqlalchemy.sql import func

# importin the mixin and adding to the user model make our user be able to use the flask login 

# message have one to many relationship with user and thread
# thread also have one to many relationship with user

class Message(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(128), nullable=False)
    message_owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'))
    date_of_creation = db.Column(db.DateTime, default = datetime.datetime.now)


class Thread(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    thread_name = db.Column(db.String(128), nullable=False)
    messages = db.relationship('Message', backref= 'thread', lazy = 'dynamic')
    thread_starter = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_of_creation = db.Column(db.DateTime, default = datetime.datetime.now)
    
    def create_message(self, message_content):
        """
        create a message in to the thread and connect with the user.id that open the thread.
        Add the message to the thread messages list
        variable:
            message_content(str)
        """
        message = Message(content = message_content, message_owner = self.thread_starter, thread_id = self.id)
        db.session.add(message)
        self.messages.append(message)
        db.session.commit()
        
    
    


# the prof_type of the user will be asigned random between the four categories. 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    name = db.Column(db.String(150))
    status = db.Column(db.String(150))
    prof_type = db.Column(db.String(54))
    image_url = db.Column(db.String(100000))
    points = db.Column(db.Integer)
    coins = db.Column(db.Integer)
    messages = db.relationship('Message', backref= 'user', lazy = 'dynamic')
    threads = db.relationship('Thread', backref = 'user', lazy = 'dynamic')
    deck_of_cards = db.relationship('Deckofcards', backref = 'user', uselist=False)
    date_of_creation = db.Column(db.DateTime, default = datetime.datetime.now)
    transactions = db.relationship('Transaction', backref= 'user', lazy = 'dynamic')


    def get_points(self, amount):
        self.points += amount

    def get_coins(self, amount):
        self.coins += amount

    def open_thread(self, thread_title):
        """
        create a thread for the user, added to the user list of threads and commit in the database
        variable thread_title is a string and will set the title
        """
        thread = Thread(thread_name = thread_title, thread_starter = self.id)
        db.session.add(thread)
        self.threads.append(thread)
        db.session.commit()

    def create_deck(self, number_of_cards):
        deck = Deckofcards()
        for i in range(number_of_cards):
            card = Futucard()
            card.create_card()
            deck.cards_on_deck.append(card)
        self.deck_of_cards = deck
        db.session.commit()
        




    
class Futucard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(150))
    specie = db.Column(db.String(150))
    age = db.Column(db.String(150))
    planet = db.Column(db.String(150))
    profession = db.Column(db.String(150))
    url = db.Column(db.String(1500000))
    rarity = db.Column(db.String(150))
    on_transaction = db.relationship('Transaction', backref = 'futucard', uselist=False)
    deck = db.Column(db.Integer, db.ForeignKey('deckofcards.id'))

    def create_card(self):
        rarity = apifile.set_random_rarity()
        character = random.choice(apifile.characters)
        self.character_name = apifile.get_name(character)
        self.specie = apifile.get_species(character)
        self.age = apifile.get_age(character)
        self.planet = apifile.get_planet_of_charac(character)
        self.profession = apifile.get_profession(character)
        self.url = apifile.get_pic_url()
        self.rarity = rarity
        db.session.add(self)
        db.session.commit()
        





    
class Deckofcards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    cards_on_deck = db.relationship('Futucard', backref = 'deckofcards', lazy='dynamic' )


    




class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_offered = db.Column(db.Integer, db.ForeignKey('futucard.id'))
    value_of_card = db.Column(db.Integer)
    card_for_trade = db.Column(db.Integer)
    transaction_creater = db.Column(db.Integer, db.ForeignKey('user.id'))

    


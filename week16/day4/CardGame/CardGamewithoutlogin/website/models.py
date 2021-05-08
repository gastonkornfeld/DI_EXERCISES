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
    have_deck = db.Column(db.String(150))
    
    def set_points(self):
        deck = self.deck_of_cards
        user_points = 0
        for card in deck:
            user_points += card.points
        self.points = user_points


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
    price = db.Column(db.Integer)
    points = db.Column(db.Integer)
    on_transaction = db.relationship('Transaction', backref = 'futucard', uselist=False)
    deck = db.Column(db.Integer, db.ForeignKey('deckofcards.id'))

    def create_card(self):
        rarity = apifile.set_random_rarity()
        if rarity == 'COMMON':
            points = random.randint(1,10) 
            price = random.randint(100,1000)
        elif rarity == 'RARE':
            price = random.randint(1000,5000)
            points = random.randint(50,100)
        elif rarity == 'EPIC':
            price = random.randint(3000,8000)
            points = random.randint(100,500)
        else:
            price = random.randint(5000,10000)
            points = random.randint(400, 1000)
        
        character = random.choice(apifile.characters)
        self.character_name = apifile.get_name(character)
        self.specie = apifile.get_species(character)
        self.age = apifile.get_age(character)
        self.planet = apifile.get_planet_of_charac(character)
        self.profession = apifile.get_profession(character)
        self.url = apifile.get_pic_url(character)
        self.rarity = rarity
        self.price = price
        self.points = points
        db.session.add(self)
        db.session.commit()
        print('card added')
        





    
class Deckofcards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    cards_on_deck = db.relationship('Futucard', backref = 'deckofcards', lazy='dynamic' )



    def delete_card(self, id):
        card = Futucard.query.get(id)
        self.cards_on_deck.remove(card)
        db.session.commit()


    def add_card(self, id):
        card = Futucard.query.get(id)
        self.cards_on_deck.append(card)
        db.session.commit()



    




class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_offered = db.Column(db.Integer, db.ForeignKey('futucard.id'))
    transaction_creater = db.Column(db.Integer, db.ForeignKey('user.id'))



    def delete(self, id):
        transaction = Transaction.query.get(id)
        db.session.delete(transaction)
        db.session.commit()


    


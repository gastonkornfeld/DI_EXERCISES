from . import db
from . import cryptoapi
from flask_login import UserMixin
from sqlalchemy.sql import func

# importin the mixin and adding to the user model make our user be able to use the flask login 
crypto_table = db.Table('cryptos',
                      db.Column('crypto_id', db.Integer, db.ForeignKey('crypto.id')),
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    cryptos = db.relationship('Crypto', secondary = crypto_table, back_populates = 'users_following')


class Crypto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(10000)) 
    symbol = db.Column(db.String(10000))
    slug = db.Column(db.String(10000)) 
    first_historical_data = db.Column(db.String(10000))
    last_historical_data = db.Column(db.String(10000))
    is_active = db.Column(db.Integer())
    price = db.Column(db.Integer())
    users_following = db.relationship('User', secondary = crypto_table, back_populates='cryptos')

    def get_info(self):
        return cryptoapi.get_info(self.id)





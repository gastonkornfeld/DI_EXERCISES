
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import User, Crypto
from . import db, cryptoapi
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required #this make the view visible only if there is a user logged in
def home():

    
        

    return render_template("home.html", user=current_user)

@views.route('/cryptos', methods=['GET', 'POST'])
@login_required #this make the view visible only if there is a user logged in
def cryptos():
    
    
    cryptos = cryptoapi.get_all_crypto()
        
        

    return render_template("cryptos.html", user=current_user, values = cryptos )



@views.route('/add-crypto/<id>', methods=['GET', 'POST'])
@login_required #this make the view visible only if there is a user logged in
def add(id):
    crypto = cryptoapi.get_crypto_data(int(id), 'id')
    id__ = id
    
    name = crypto[0]['name']
    symbol = crypto[0]['symbol']
    slug = crypto[0]['slug']
    last_historical_data = crypto[0]['last_historical_data'][0:10]
    first_historical_data = crypto[0]['first_historical_data'][0:10]
    is_active = crypto[0]['is_active']
    price = round(cryptoapi.crypto_price(id), 2)

    new_crypto = Crypto(id = id__, name = name, symbol = symbol, slug = slug, 
                            last_historical_data = last_historical_data, 
                            first_historical_data = first_historical_data,
                            is_active = is_active, price = price)

    db.session.add(new_crypto)
    current_user.cryptos.append(new_crypto)
    db.session.commit()



        

    return redirect(url_for('views.home'))



@views.route('/details/<id>', methods=['GET', 'POST'])
@login_required #this make the view visible only if there is a user logged in
def details(id):
    crypto = cryptoapi.get_crypto_data(int(id), 'id')
    price = round(cryptoapi.crypto_price(id), 2)
    other_details = cryptoapi.get_details(id)
        

    return render_template("details.html", user=current_user, value = crypto, price = price, details = other_details)




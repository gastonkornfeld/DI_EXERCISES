
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, session
from flask_login import login_required, current_user
from . import models, forms
from . import db
import json
from sqlalchemy import desc
views = Blueprint('views', __name__)


@views.route("/")
def activate():
    session['id_user_logged'] = 0
    return redirect(url_for('views.home'))


@views.route("/index")
# @login_required
def home():
    form = forms.LoginForm()
    

    if session['id_user_logged'] != 0:

        user_id = int(session['id_user_logged'])
        user = models.User.query.get(user_id)
        return render_template('homepage.html', user = user)
    flash('please login', 'danger')
    return render_template('login.html', form = form)




@views.route("/profile/<int:id>")
# @login_required
def profile(id):
    user = models.User.query.get(id)

    

    return render_template('profile.html', user = user)


@views.route("/threads", methods = ["GET", "POST"])
# @login_required
def threads():
    """
    in this view the user can see all the avaiables threads and add another one
    will be redirected to the same page. 
    """
    user_id = int(session['id_user_logged'])
    user = models.User.query.get(user_id)
    threads = models.Thread.query.all()
    form = forms.CreateThreadForm()
    user_model = models.User
    if form.validate_on_submit():
        title = form.name.data
        user.open_thread(title)
        
        return redirect(url_for('views.threads'))
    return render_template('threads.html', user = user, threads = threads, form = form, User = user_model)
    



@views.route("/thread/<int:id>", methods = ['GET', 'POST'])
# @login_required
def view_thread(id):
    """
    when the user click on a thread get redirect to the thread details show in this route. 
    show all the messages inside a thread and get the user a way to add messages in the thread.
    for admin users will display also a button to delete messages and close threads 
    """

    user_logged_id = int(session['id_user_logged'])
    user_logged = models.User.query.get(user_logged_id)
    thread = models.Thread.query.get(id)
    user_starter = models.User.query.get(thread.thread_starter)
    form = forms.CreateMessageForm()
    user_model = models.User
    if request.method == 'POST':
        content = form.name.data
        message = models.Message(content = content, message_owner = int(session['id_user_logged']) , thread_id = thread.id)
        db.session.add(message)
        thread.messages.append(message)
        db.session.commit()
        return render_template('thread_details.html', thread = thread, user = user_starter, form = form, User = user_model, user_logged = user_logged)


    return render_template('thread_details.html', thread = thread, user = user_starter, form = form, User = user_model, user_logged = user_logged)


@views.route("/delete-thread/<int:id>", methods = ['GET', 'POST'])
def delete_thread(id):
    """
    This route is only available for admin usage. take the id of the thread and delete it.
    """
    thread = models.Thread.query.get(id)
    thread.deletee()

    return redirect(url_for('views.threads'))

@views.route("/delete-message/<int:id>", methods = ['GET', 'POST'])
def delete_message(id):
    """
    This route is only available for admin usage. take the id of the message and delete it.
    """
    
    message = models.Message.query.get(id)
    thread = models.Thread.query.get(message.thread_id)
    message.deletee()


    return redirect(url_for('views.view_thread', id = thread.id))





@views.route("/deck/<int:user_id>", methods = ['GET', 'POST'])
def deck(user_id):

    user_logged_id = int(session['id_user_logged'])
    user_logged = models.User.query.get(user_logged_id)
    
    
    user = models.User.query.get(user_id)
    deck = user.deck_of_cards


    



    return render_template('user_deck.html', user = user, deck = deck, user_logged = user_logged)


@views.route("/get-deck", methods = ['GET', 'POST'])
def get_deck():
    user_id = int(session['id_user_logged'])
    user = models.User.query.get(user_id)
    user.create_deck(20)
    user.have_deck = 'yes'
    
    return redirect(url_for('views.home'))





@views.route("/trade/<int:id1>")
def coin_trade(id1):
    user_id = int(session['id_user_logged'])
    user = models.User.query.get(user_id)
    user_deck = user.deck_of_cards
    card = models.Futucard.query.get(id1)
    if user.deck_of_cards.id == card.deck:
        transaction = models.Transaction(card_offered = id1, transaction_creater = user_id)
        db.session.add(transaction)
        db.session.commit()

        user_deck.delete_card(id1)
    
        flash('Card added to the market', 'success')
        return redirect(url_for('views.deck', user_id = user_id))
    else: 
        flash('invalid-method', 'danger')
        return redirect(url_for('views.market', user_id = user_id))





@views.route("/market")
def market():
    user_id = int(session['id_user_logged'])
    user1 = models.User.query.get(user_id)
    transactions = models.Transaction.query.all()
    futucard_model = models.Futucard
    users_model = models.User
    return render_template('market.html', transactions = transactions, Card = futucard_model, User = users_model, user_logged = user1)




@views.route("/complete_transaction/<int:transaction_id>")
def complete_transaction(transaction_id):
    user_id = int(session['id_user_logged'])
    user = models.User.query.get(user_id)
    user_deck = user.deck_of_cards

    transaction = models.Transaction.query.get(transaction_id)
    card_seller = models.User.query.get(transaction.transaction_creater)

    card_on_sale = models.Futucard.query.get(transaction.card_offered)
    


    price = card_on_sale.price
    if user.coins >= price:

        points = card_on_sale.points
        card_seller.get_coins(round(price*0.90,2))
        user.get_coins(-price)
        user.get_points(round(points*0.7,2))
        card_seller.get_points(round(points*0.3,2))
        user_deck.add_card(transaction.card_offered)
        db.session.delete(transaction)
        db.session.commit()
    
# chek if the buyer is the same than the seller

        return redirect(url_for('views.market'))
    flash('you dont have enough coins', 'danger')
    return redirect(url_for('views.market'))




@views.route("/leaderboard")
def leaderboard():
    point_leaders = models.User.query.order_by(desc(models.User.points)).all()
    coins_leaders = models.User.query.order_by(desc(models.User.coins)).all()
    amount_of_cards_leaders = models.get_user_with_more_cards()
    return render_template('leaderboards.html',  users = point_leaders, users1 = coins_leaders, users2 = amount_of_cards_leaders )




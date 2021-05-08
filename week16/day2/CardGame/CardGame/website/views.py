
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




    

 





@views.route("/profile/<int:id>")
@login_required
def profile(id):
    user = models.User.query.get(id)

    

    return render_template('profile.html', user = user)


@views.route("/threads", methods = ["GET", "POST"])
@login_required
def threads():
    """
    in this view the user can see all the avaiables threads and add another one
    will be redirected to the same page. 
    """
    user = current_user
    threads = models.Thread.query.all()
    form = forms.CreateThreadForm()
    user_model = models.User
    if form.validate_on_submit():
        title = form.name.data
        user.open_thread(title)
        
        return redirect(url_for('views.threads'))
    return render_template('threads.html', user = current_user, threads = threads, form = form, User = user_model)
    



@views.route("/thread/<int:id>", methods = ['GET', 'POST'])
@login_required
def view_thread(id):
    """
    when the user click on a thread get redirect to the thread details show in this route. 
    show all the messages inside a thread and get the user a way to add messages in the thread.
    for admin users will display also a button to delete messages and close threads 
    """
    thread = models.Thread.query.get(id)
    user_starter = models.User.query.get(thread.thread_starter)
    form = forms.CreateMessageForm()
    user_model = models.User
    if request.method == 'POST':
        content = form.name.data
        message = models.Message(content = content, message_owner = current_user.id , thread_id = thread.id)
        db.session.add(message)
        thread.messages.append(message)
        db.session.commit()
        return render_template('thread_details.html', thread = thread, user = user_starter, form = form, User = user_model)


    return render_template('thread_details.html', thread = thread, user = user_starter, form = form, User = user_model)




    
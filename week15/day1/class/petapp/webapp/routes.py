import flask


from . import app, filters
from . import models
from . import db


@app.route("/")
def index():
    return flask.render_template('index.html')


@app.route("/pets")
def pets():
    
    pets = models.Pet.query.all()
    return flask.render_template('pets.html' ,pets = pets)

@app.route('/add')
def add():
    cart = models.Cart.query.get(1)
    change = models.Pet.query.get(1)
    cart.pets.append(change)
    # cart = models.Cart()
    # db.session.add(cart)
    db.session.commit()
    return flask.redirect(flask.url_for('pets'))


@app.route('/pet/<int:pet_id>')
def pet_details(pet_id):
    pet_details =  models.Pet.query.get(pet_id)
    
    return flask.render_template('pet.html', pet = pet_details)

@app.route('/cart')
def cart():
    cart = models.Cart.query.get(1)
    total = 0
    for item in cart.pets:  
        total = total + item.price


    return flask.render_template('cart.html', cart = cart, total = total)

# add a pet to the cart
@app.route('/add_pet/<int:pet_id>')
def add_pet(pet_id):
    cart = models.Cart.query.get(1)
    pet =  models.Pet.query.get(pet_id)
    cart.pets.append(pet)
    db.session.commit()
    flask.flash(f'Added to the cart with exit', 'success')
    return flask.redirect(flask.url_for('cart'))


# delete a pet from the cart
@app.route('/delete_pet/<int:pet_id>')
def delete_pet(pet_id):
    cart = models.Cart.query.get(1)
    pet =  models.Pet.query.get(pet_id)
    cart.pets.remove(pet)
    db.session.commit()
    flask.flash(f'Deleted succesfully', 'success')
    return flask.redirect(flask.url_for('cart'))

from . import db





class Cart(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    pets = db.relationship('Pet', backref= 'cart', lazy= 'dynamic') 

    def add_to_cart(self, pet_id):
        pet = Pet.query.get(pet_id)
        self.pets.append(pet) 

class Pet(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.String(64), nullable=False)
    breed = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer())
    details = db.Column(db.Text())
    image = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer())
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))


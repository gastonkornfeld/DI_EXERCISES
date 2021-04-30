from . import db






class User(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    street = db.Column(db.String(64))
    city = db.Column(db.String(64))
    zip_code = db.Column(db.Integer())

    # def __init__(self, name, street, city, zip_code):
    #     self.name = name
    #     self.city = city
    #     self.street = street
    #     self.zip_code = zip_code






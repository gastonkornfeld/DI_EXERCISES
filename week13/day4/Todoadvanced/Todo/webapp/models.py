
from . import db
class Todo(db.Model):
    
    id = db.Column(db.Integer(), primary_key=True)
    details = db.Column(db.String(200))
    image = db.relationship('Image', uselist=False,  backref= 'todo')


class Image(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String(10000))
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'))

    



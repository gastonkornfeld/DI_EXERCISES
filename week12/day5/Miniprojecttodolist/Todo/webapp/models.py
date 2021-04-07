
from . import db
class Todo(db.Model):
    
    id = db.Column(db.Integer(), primary_key=True)
    details = db.Column(db.String(200))
    completed = db.Column(db.Boolean())
    



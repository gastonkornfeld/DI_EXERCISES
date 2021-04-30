import flask
import flask_sqlalchemy
import flask_migrate
import os



app = flask.Flask(__name__)

# In case you have: "A secret key is required to use..."
app.config["SECRET_KEY"] = "1e447e934b371d2826cb840141b47703"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)





from . import routes, models, funct

all_users = models.User.query.all() 


db_inf = funct.getJSON('webapp/static/users.json')
def populate():
        
    for user in db_inf:
        name = user['name']
        street = user['address']['street']
        city = user['address']['city']
        # zip_code = str(user['address']['zipcode'])
        new_data = models.User(name = name, street = street, city = city, zip_code = 1)
        db.session.add(new_data)
        db.session.commit()


# populate(), already called twice ups

# new_data = User(name, email)
# db.session.add(new_data)
# db.session.commit()

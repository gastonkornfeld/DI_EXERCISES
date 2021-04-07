import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os



app = flask.Flask(__name__)



# In case you have: "A secret key is required to use..."
app.config["SECRET_KEY"] = "1e447e934b371d2826cb840141b49603"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app2.sqlite')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from . import routes, models

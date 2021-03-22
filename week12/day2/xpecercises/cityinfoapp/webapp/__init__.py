import flask

app = flask.Flask(__name__)

# In case you have: "A secret key is required to use..."
app.config["SECRET_KEY"] = "1e447e934b371d2826cb840141b49703"

from . import routes
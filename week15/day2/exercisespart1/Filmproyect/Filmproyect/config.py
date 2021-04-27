


basedir = os.path.abspath(os.path.dirname(__file__))

class Config():

    DEBUG = True
    SECRET_KEY = "1e447e934b371d282acb841141b47703"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'petstore2.sqlite')

    BASEDIR = basedir

from webapp import create_app
from . import config


app = create_app(config.current_config)
app.run(port = 5002, debug = True)



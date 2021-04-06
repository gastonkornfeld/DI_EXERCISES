import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import forms

app = flask.Flask(__name__)



# In case you have: "A secret key is required to use..."
app.config["SECRET_KEY"] = "1e447e934b371d2826cb840141b49603"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/todolist"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route("/")
@app.route("/home")
def home():
    return flask.render_template('home.html')


@app.route('/add', methods=["POST"])
def add():
    todo = Todo(text = flask.request.form['todoitem'], complete = False)
    db.session.add(todo)
    db.session.commit()

    return flask.redirect(flask.url_for('home'))


@app.route('/register', methods=['GET', "POST"])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        flask.flash(f'Account created for {form.username.data}!', 'success')
        return flask.redirect(flask.url_for('home'))
    return flask.render_template('register.html', title = 'Register', form = form)


@app.route('/login',  methods=['GET', "POST"])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'gatok37@gmail.com' and form.password.data == 'kornfeld':
            flask.flash("You have been logged in!!", 'success')
            return flask.redirect(flask.url_for('home'))
        else:
            flask.flash("Log In Unsuccessful. Please check username and password", 'danger')
    return flask.render_template('login.html', title = 'Login', form = form)



@app.route('/about')
def about():
    return flask.render_template('about.html', title = 'About')

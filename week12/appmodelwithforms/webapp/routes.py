import flask

from . import app       # . is webapp/
from . import forms


@app.route("/")
@app.route("/home")
def home():
    return flask.render_template('home.html')


@app.route('/about')
def about():
    return flask.render_template('about.html', title = 'About')




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

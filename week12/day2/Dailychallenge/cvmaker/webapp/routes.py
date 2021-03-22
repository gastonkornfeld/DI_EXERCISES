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




@app.route('/cv_template', methods=['GET', "POST"])
def cv_template():
    form = forms.CvForm()
    if form.validate_on_submit():
        flask.flash(f'CV created for {form.complete_name.data}!', 'success')
        return flask.render_template('cv_example.html', form = form)
    return flask.render_template('cvtemplate.html', title = 'Cv template', form = form)



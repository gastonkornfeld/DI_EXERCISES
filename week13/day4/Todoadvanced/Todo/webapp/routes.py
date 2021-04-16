
import flask

from . import app       
from . import models
from . import forms
from . import db


@app.route('/', methods=['GET', "POST"])
@app.route('/index', methods=['GET', "POST"])
def index():
    
    all_task = models.Todo.query.all()
    
    form = forms.AddTodoForm()
    if form.validate_on_submit():
        content = form.task.data
        image = models.Image(url = form.image.data)
        task1 = models.Todo(details = content, image = image)
        db.session.add(task1)
        db.session.commit()
        flask.flash(f'Task added to the list', 'success')
        return flask.redirect(flask.url_for('index'))
    return flask.render_template('index.html', title = 'Home', form = form, tasks = all_task)


@app.route('/complete/<todo_id>')
def complete(todo_id):
    taks_finished = models.Todo.query.get(todo_id)
    db.session.delete(taks_finished)
    db.session.commit()
    return flask.redirect(flask.url_for('index'))


@app.route('/delete_all')
def delete():
    all_task = models.Todo.query.all()
    for task in all_task:
        db.session.delete(task)
        db.session.commit()
    return flask.redirect(flask.url_for('index'))


@app.route('/about')
def about():
    return flask.render_template('about.html', title = 'About')


# @app.route('/add', methods=["POST"])
# def add():
    

#     return flask.redirect(flask.url_for('home'))




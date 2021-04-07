  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo






class AddTodoForm(FlaskForm):
    task = StringField('Task',
                        validators=[DataRequired(), Length(max=200)])
    complete = BooleanField()
    submit = SubmitField('ADD')

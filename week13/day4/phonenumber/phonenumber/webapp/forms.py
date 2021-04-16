  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import phonenumbers






class PersonForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='put a valid email')])
    address = StringField('Address')
    phone = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Submit')


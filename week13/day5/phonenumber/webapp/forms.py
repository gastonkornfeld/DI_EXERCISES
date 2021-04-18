  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import phonenumbers






class PersonForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='put a valid email')])
    address = StringField('Address')
    phone = StringField('Phone', validators=[DataRequired()])
    nationality = StringField('Born Country') 
    submit = SubmitField('Submit')



class Search_nameForm(FlaskForm):
    name = StringField('Name To Search', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Search_nationalityForm(FlaskForm):
    nationality = StringField('Nationality To Search', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Search_numberForm(FlaskForm):
    number = StringField('Number To Search', validators=[DataRequired()])
    submit = SubmitField('Submit')
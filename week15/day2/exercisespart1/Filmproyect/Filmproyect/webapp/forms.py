  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError







class AddFilmForm(FlaskForm):

    name = StringField('Film Title', validators=[DataRequired()])
    
    year = StringField('Date of release', validators=[DataRequired()])
    created_in = StringField('Country of creation', validators=[DataRequired()])
    categories = StringField('ADD categories separated by ","', validators=[DataRequired()])
    director = StringField('Imput Director Name, Last name ', validators=[DataRequired()])
    submit = SubmitField('Submit')



class AddDirectorForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


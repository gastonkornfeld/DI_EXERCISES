  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange






class AddCityForm(FlaskForm):
    name = StringField('City Name',
                        validators=[DataRequired(), Length(max=15)])
    country = StringField('Country',
                        validators=[DataRequired()])
    habitants = IntegerField('Numbers of Habitants', validators=[DataRequired(), NumberRange(min=0)]) 
    area = IntegerField('area, in square meters', validators=[DataRequired()])
    latitude = StringField('Latitude')
    longitude = StringField('Longitude')
    capital = BooleanField("Capital")
    submit = SubmitField('Add')


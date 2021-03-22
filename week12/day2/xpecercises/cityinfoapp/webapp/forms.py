  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo






class AddCityForm(FlaskForm):
    name = StringField('City Name',
                        validators=[DataRequired(), Length(max=15)])
    country = StringField('Country',
                        validators=[DataRequired()])
    habitants = IntegerField('Numbers of Habitants', validators=[DataRequired()]) 
    area = IntegerField('area, in square meters', validators=[DataRequired()])
    submit = SubmitField('Add')

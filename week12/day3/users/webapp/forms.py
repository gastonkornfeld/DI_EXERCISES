  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Create a file called forms.py that will hold our “AddUser” form. This form should have a few inputs:
# user_name : StringField
# street : StringField
# city : StringField
# zipcode : IntegerField
# a button : SubmitField
# You can add some validators to the form fields if you want :)

class AddUserForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)])
    street = StringField('Street',
                        validators=[DataRequired()])
    city = StringField('City',
                        validators=[DataRequired()])

    zipcode = IntegerField('Zipcode',
                        validators=[DataRequired()])
    submit = SubmitField('ADD USER')


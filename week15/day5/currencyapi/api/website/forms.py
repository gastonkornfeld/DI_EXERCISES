  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class SignUpForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password1 = StringField('Password',
                        validators=[DataRequired()])
    password2 = StringField('Repeat password',
                        validators=[DataRequired(), EqualTo(password1)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=2, max=20)])
    password = StringField('Password',
                        validators=[DataRequired()])
    submit = SubmitField('Login')


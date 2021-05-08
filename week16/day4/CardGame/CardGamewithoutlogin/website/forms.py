  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class SignUpForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password1 = PasswordField('Password',
                        validators=[DataRequired()])
    password2 = PasswordField('Repeat password',
                        validators=[DataRequired(), EqualTo(password1)])
    name = StringField('Complete Name',
                        validators=[DataRequired(), Length(min=2, max=20)])
    image_url = StringField('Profile picture url',
                        validators=[DataRequired(), Length(min=2, max=100000)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=2, max=20)])
    password = PasswordField('Password',
                        validators=[DataRequired()])
    submit = SubmitField('Login')




class CreateThreadForm(FlaskForm):
    name = StringField('WRITE AN ENTRY TO START A THREAD', validators=[DataRequired(), Length(min=2, max=2000)])
    
    submit = SubmitField('Open Thread')

class CreateMessageForm(FlaskForm):
    name = StringField('Message Content', validators=[DataRequired(), Length(min=2, max=2000)])
    
    submit = SubmitField('Add message to the thread')


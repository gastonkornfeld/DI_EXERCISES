  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
# Form class --> flask_wtf.FlaskForm
# Form fields --> wtforms.SomethingField

# each form is a class inheriting from flask_wtf.FlaskForm
# every class attribute is a field in the form

# For example:
# A form with two fields:
#   - A name
#   - An age



class CvForm(FlaskForm):
    complete_name = StringField('Complete Name',
                        validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    studies = StringField('Degree Title',
                        validators=[DataRequired()])

    work = StringField('Resume Your work experience in 300 Characters',
                        validators=[DataRequired(), Length(min=20, max=300)])
    position = StringField('Wich position you are applying for',
                        validators=[DataRequired()])
    submit = SubmitField('Create CV')


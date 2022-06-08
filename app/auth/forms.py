from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, FileField
from wtforms import validators
from wtforms.validators import Email, EqualTo, ValidationError, DataRequired




class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    passwrod = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Save_myself')
    submit = SubmitField('Sing in')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')


class LoadForm(FlaskForm):
    submit = SubmitField('Submit')

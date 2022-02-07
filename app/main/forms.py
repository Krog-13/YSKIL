from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, FileField
from wtforms import validators
from wtforms.validators import Email, EqualTo, ValidationError, DataRequired


class UploadForm(FlaskForm):
    file = FileField('File PDF')
    submit = SubmitField('Load')


class PostForm(FlaskForm):
    subject = TextAreaField('Enter you subject:', validators=[DataRequired()])
    body = TextAreaField('describe', validators=[DataRequired()])
    doc = FileField('File')
    submit = SubmitField('Submit')
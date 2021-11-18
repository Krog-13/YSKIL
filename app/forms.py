from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, FileField
from wtforms.validators import ValidationError, DataRequired


class UploadForm(FlaskForm):
    file = FileField('File PDF')
    submit = SubmitField('Load')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')


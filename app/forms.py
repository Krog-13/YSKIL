from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, FileField
from wtforms.validators import ValidationError, DataRequired


class UploadForm(FlaskForm):
    file = FileField('File PDF')
    submit = SubmitField('Load')


class PostForm(FlaskForm):
    subject = TextAreaField('Enter you subject:', validators=[DataRequired()])
    body = TextAreaField('describe', validators=[DataRequired()])
    cirtify = FileField('PDF file')
    submit = SubmitField('Submit')


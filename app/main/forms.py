from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, FileField,RadioField, DateField
from wtforms import validators
from wtforms.validators import Email, EqualTo, ValidationError, DataRequired


class UploadForm(FlaskForm):
    file = FileField('File PDF')
    submit = SubmitField('Load')


class PostForm(FlaskForm):
    subject = TextAreaField('Enter you subject:', validators=[DataRequired()])
    body = TextAreaField('describe', validators=[DataRequired()])
    summary = FileField('File')
    submit = SubmitField('Submit')


class TalentForm(FlaskForm):
    # lvl = ['Easy', 'Medium', 'Hard']
    doc = FileField('Certificate')
    title = StringField('Name')
    datetime = DateField('Date of receipt', format='%Y-%m-%d', validators=(validators.Optional(),))
    organisation = StringField('Organization')
    submit = SubmitField('Accept')
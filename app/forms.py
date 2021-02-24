from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import (
    InputRequired,
    DataRequired,
    Email,
    EqualTo,
    ValidationError,
    Length)


class ContactForm(FlaskForm):

    name = StringField('Name', validators = [InputRequired(message="Please enter your name")])

    email = EmailField('Email Address', validators = [InputRequired(message="Please nter your email address")])

    subject = StringField('Subject', validators = [InputRequired(message="Please enter the subject for your message")])

    message_body = TextAreaField('Message Body' , kender_kw={ "rows": 8, "cols": 50}) 

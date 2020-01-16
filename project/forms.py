from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.fields.html5 import DateField

class PasswordForm(FlaskForm):
    password = PasswordField("password", validators=[validators.Required()])
    submit = SubmitField("Login")

class DdayForm(FlaskForm):
    name = StringField("name", validators=[validators.Required()])
    date = DateField("date", validators=[validators.Required()])
    submit = SubmitField("add")
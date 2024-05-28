from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class SignUpForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired()], render_kw={'placeholder': 'Firstname', 'size': '35'})
    lastname = StringField('Lastname', validators=[DataRequired()], render_kw={'placeholder': 'Lastname', 'size': '35'})
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'Username', 'size': '35'})
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email', 'size': '35'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password', 'size': '35'})
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo(password)], render_kw={'placeholder': 'Confirm Password', 'size': '35'})
    submit = SubmitField('Sign UP', render_kw={'class': 'submit-button'})

class LoginForm(FlaskForm):
    username = username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'Username', 'size': '35'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password', 'size': '35'})
    submit = SubmitField('Login', render_kw={'class': 'submit-button'})
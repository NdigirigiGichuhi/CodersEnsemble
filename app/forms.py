from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo
from datetime import datetime


class SignUpForm(FlaskForm):
    """
    Form for users to create a new account.
    """
    firstname = StringField(
        'Firstname',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Firstname', 'size': '35'}
    )
    lastname = StringField(
        'Lastname',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Lastname', 'size': '35'}
    )
    username = StringField(
        'Username',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Username', 'size': '35'}
    )
    email = EmailField(
        'Email',
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'Email', 'size': '35'}
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Password', 'size': '35'}
    )
    confirm_pass = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')],
        render_kw={'placeholder': 'Confirm Password', 'size': '35'}
    )
    submit = SubmitField(
        'Sign UP',
        render_kw={'class': 'submit-button'}
    )


class LoginForm(FlaskForm):
    """
    Form for users to log in to their account.
    """
    username = StringField(
        'Username',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Username', 'size': '35'}
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Password', 'size': '35'}
    )
    submit = SubmitField(
        'Login',
        render_kw={'class': 'submit-button'}
    )

class EditProfileForm(FlaskForm):
    """
    Form for editing the user profile.
    """
    firstname = StringField(
        'Firstname',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Firstname', 'size': '35'}
    )
    lastname = StringField(
        'Lastname',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Lastname', 'size': '35'}
    )
    username = StringField(
        'Username',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Username', 'size': '35'}
    )
    email = EmailField(
        'Email',
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'Email', 'size': '35'}
    )
    password_hash = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Password', 'size': '35'}
    )
    confirm_pass = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password_hash')],
        render_kw={'placeholder': 'Confirm Password', 'size': '35'}
    )
    submit = SubmitField(
        'Update Profile',
        render_kw={'class': 'submit-button'}
    )

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField("What's happening")
    date_posted = DateTimeField('Date_posted', format='%Y-%m-%d %H:%M', default=datetime.utcnow, validators=[DataRequired()])
    post = SubmitField('Post')


class EditPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField("What's happening")
    updated_at = DateTimeField('Date_posted', format='%Y-%m-%d %H:%M', default=datetime.utcnow, validators=[DataRequired()])
    post = SubmitField('Edit Post')


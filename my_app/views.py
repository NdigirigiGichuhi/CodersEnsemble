from my_app import app
from flask import render_template
from my_app.forms import SignUpForm


@app.route('/')
def index():
    form = SignUpForm()
    return render_template('landing.html', form=form)


@app.route('/home')
def home():
    return render_template('home.html')
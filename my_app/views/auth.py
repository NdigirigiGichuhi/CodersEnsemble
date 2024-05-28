from app import app, db
from flask import render_template, redirect, url_for, flash, Blueprint
from app.forms import SignUpForm, LoginForm
from models import User
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['POST', 'GET'])
def index():
    form = SignUpForm()

    if form.validate_on_submit():
        user = User(firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    username=form.username.data,
                    email=form.email.data,
                    password_hash = form.password.data)
        
        db.session.add(user)
        db.session.commit()

        flash('Registration successful')
        return redirect(url_for('login'))
    
    return render_template('landing.html', form=form)


@auth_bp.route('/home')
@login_required
def home():
    return render_template('home.html')


@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user(user)
    return redirect(url_for('landing'))

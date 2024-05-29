from flask import render_template, redirect, url_for, flash, Blueprint
from app import db
from app.forms import SignUpForm, LoginForm
from flask_login import login_user
from app.models import User
from bcrypt import hashpw, gensalt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['POST', 'GET'])
def index():
    form = SignUpForm()

    if form.validate_on_submit():
        try:
            hashed_password = hashpw(form.password.data.encode('utf-8'), gensalt())
            user = User(
                firstname=form.firstname.data,
                lastname=form.lastname.data,
                username=form.username.data,
                email=form.email.data,
                password_hash=hashed_password.decode('utf-8')
            )
            db.session.add(user)
            db.session.commit()
            flash('Registration successful')
            return redirect(url_for('auth.login'))  
        except Exception as e:
            db.session.rollback()
            flash('An error occurred: {}'.format(e))
            print(e)
            return redirect(url_for('auth.index'))  
    return render_template('landing.html', form=form)

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and hashpw(form.password.data.encode('utf-8'), user.password_hash.encode('utf-8')) == user.password_hash.encode('utf-8'):
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@auth_bp.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')
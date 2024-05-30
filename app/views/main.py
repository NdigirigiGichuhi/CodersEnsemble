from flask import render_template, redirect, url_for, flash, Blueprint
from app import db
from app.forms import SignUpForm, LoginForm, EditProfileForm
from flask_login import login_user, logout_user, login_required
from app.models import User
from bcrypt import hashpw, gensalt

main_bp = Blueprint('main', __name__)


@main_bp.route('/profile', methods=['GET'])
def display_profile():
    return render_template('user/profile.html')

@main_bp.route('/edit-profile', methods=['POST', 'GET'])
def update_profile():
    form = EditProfileForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.password = form.password.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('main.display_profile'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.password.data = current_user.password
        
    return render_template('user/update_profile.html', form=form)
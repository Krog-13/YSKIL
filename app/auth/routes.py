from app import db
from app.auth import bp
from flask import request, redirect, url_for, flash, render_template, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app.auth.forms import LoginForm, RegisterForm
from app.models import Achievements, User





@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.passwrod.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me)
        return redirect(url_for('mian.index'))
    return render_template('auth/login.html', title='Sing in', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations you are now a registered user!')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', title='Register', form=form)



@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))



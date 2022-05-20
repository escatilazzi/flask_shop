from flask import render_template, flash, redirect, url_for, Blueprint, request
from flask_login import current_user, login_user, logout_user
from src.account.forms import LoginForm, RegistrationForm
from src.models import User
from src.database import db_session

account_bp = Blueprint('account',__name__)

@account_bp.route('/account/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('account.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('account/login.html', title='Sing In', form=form)

@account_bp.route('/account/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db_session.add(new_user)
        db_session.commit()
        return redirect(url_for('account.login'))
    return render_template('account/register.html', form=form)

@account_bp.route('/account/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

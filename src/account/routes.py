from flask import abort, render_template,flash, redirect, url_for, Blueprint, request, session
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse
from src.account.forms import LoginForm, RegistrationForm
from src.models import User, Role, UserRoles
from src import db

account_bp = Blueprint('account',__name__)

@account_bp.route('/account/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('account.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('public.home'))
    return render_template('account/login.html', title='Login', form=form)


@account_bp.route('/account/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, roles=[Role.query.filter_by(name='Guest').first()])
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registered successfully!')
        return redirect(url_for('account.login'))
    return render_template('account/register.html', form=form)

@account_bp.route('/account/logout')
def logout():
    logout_user()
    return redirect(url_for('public.home'))

@account_bp.route('/account/profile', methods=['GET','POST'])
@login_required
def profile():
    return render_template('account/profile.html', title='Profile')
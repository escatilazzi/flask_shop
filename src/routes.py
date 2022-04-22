from flask import render_template, flash, redirect, url_for
from src import app
from src.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, rememberme={}'.format(form.usr_name.data, form.rememberme.data))
        return redirect(url_for('index'))
    return render_template('auth/login.html', title='Sign In', form=form)



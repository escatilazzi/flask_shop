from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    usr_name = StringField('username', validators=[DataRequired()])
    usr_pass = PasswordField('password', validators=[DataRequired()])
    rememberme = BooleanField('Remember')
    submit = SubmitField('sing in')
    

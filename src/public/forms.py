from ast import Sub
from tkinter.tix import Select
from tokenize import String
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, FloatField, FileField, IntegerField, MultipleFileField, SelectField,TextAreaField
from wtforms.validators import DataRequired, Length, InputRequired,  Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    telephone = IntegerField('Telefono', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    message = TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField("Enviar")
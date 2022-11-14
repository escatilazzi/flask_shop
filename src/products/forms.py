from ast import Sub
from tkinter.tix import Select
from tokenize import String
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, FloatField, FileField, IntegerField, MultipleFileField, SelectField
from wtforms.validators import DataRequired, Length, InputRequired

class AddComment(FlaskForm):
    comment = StringField("", validators=[DataRequired(), Length(max=5000)])
    submit= SubmitField("Agregar comentario")
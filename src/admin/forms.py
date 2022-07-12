from ast import Sub
from tkinter.tix import Select
from tokenize import String
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, FloatField, FileField, IntegerField, MultipleFileField, SelectField
from wtforms.validators import DataRequired, Length, InputRequired

class AddCategory(FlaskForm):
    name = StringField("Categoria:", validators=[DataRequired(), Length(max=60)])
    submit= SubmitField("Agregar categoria")

class AddBrand(FlaskForm):
    name = StringField("Marca:" ,validators=[DataRequired()])
    submit = SubmitField("Agregar marca")

class AddDiscount(FlaskForm):
    name= StringField("Descuento: ")
    percent=  IntegerField("Porcentaje: ", validators=[DataRequired()])
    submit = SubmitField("Agregar descuento")

class AddProduct(FlaskForm):
    name= StringField("Nombre de Producto", validators=[DataRequired(), Length(max=160)])
    price= FloatField("Precio", validators=[DataRequired()])
    description= StringField("Descripcion", validators=[DataRequired()])
    category= SelectField('Categoria', coerce=int, validate_choice=False)
    inventory= IntegerField("ID Inventory ")
    brand = SelectField('Marca', coerce=int, validate_choice=False)
    discount=  SelectField('Descuento', coerce=int, validate_choice=False)
    image = MultipleFileField('Imagenes de producto', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Images only!'),Length(min=1 , max=5, message="")] )
    submit= SubmitField("Agregar producto")
    



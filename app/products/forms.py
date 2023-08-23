from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

#Formulario de registro de nuevo producto
class NewProductForm(FlaskForm):
    nombre = StringField("Ingresa el nombre: ")
    precio = StringField("Ingresa el precio: ")
    submit = SubmitField("Registrar")
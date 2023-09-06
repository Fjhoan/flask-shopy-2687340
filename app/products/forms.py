from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from flask_wtf.file import FileField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileAllowed, FileRequired

#Formulario de registro de nuevo producto
class NewProductForm(FlaskForm):
    nombre = StringField(validators=[ InputRequired(message="Falta el nombre") ],
                        label="Ingresa el nombre: ")
    precio = IntegerField(label="Ingresa el precio: ", 
                        validators=[ InputRequired(message="precio requerido"),
                                    NumberRange(message="precio fuera de rango", min= 1000, max= 10000)
                                    ])
    imagen = FileField(label="cargue imagen del producto:",
                        validators=[
                            FileRequired(
                                message="Suba una imagen"
                            ),
                            FileAllowed(
                                ["jpg","png"],
                                message="Tipo de archivo incorrecto"
                            )
                        ])
    submit = SubmitField("Registrar")
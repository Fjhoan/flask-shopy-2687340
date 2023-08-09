#dependencia de flask
from flask import Flask, render_template 
#dependencia de modelos
from flask_sqlalchemy import SQLAlchemy
#dependencia de la migraciones
from flask_migrate import Migrate
#dependencia para fecha y hora
from datetime import datetime
#dependencias de wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

#crear el objeto Flask
app = Flask(__name__)
#definir la 'cadena de conexión' (conetion string) para el proyecto
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ficha2687340q'

#crear el objeto de los modelos
db = SQLAlchemy(app)

#crear el objeto de migración
migrate = Migrate(app, db)

#crear el formulario de producto
class ProductosForm(FlaskForm):
    nombre = StringField('Ingrese nombre producto')
    precio = StringField('Ingrese precio producto')
    submit = SubmitField('Ingrese registrar producto')

#crear los modelos:
class Cliente(db.Model):
    #definir los atributos 
    __tablename__ = "clientes"
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(120) , nullable = True)
    password = db.Column(db.String(128) , nullable = True)
    email = db.Column(db.String(120) , nullable = True)
        #Relaciones en SQL alchemy
    ventas = db.relationship('Venta', backref = "cliente", lazy = "dynamic")


#Crear modelo producto
class Producto(db.Model):
    #definir los atributos 
    __tablename__ = "productos"
    id = db.Column(db.Integer , primary_key = True)
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(200))

#Crear modelo producto
class Venta(db.Model):
    #definir los atributos 
    __tablename__ = "ventas"
    id = db.Column(db.Integer , primary_key = True)
    fecha = db.Column(db.DateTime , default = datetime.utcnow)
    #clave foránea:
    cliente_id = db.Column(db.Integer , db.ForeignKey('clientes.id'))

class Detalles(db.Model):
    __tablename__ = "detalles"
    id = db.Column(db.Integer , primary_key = True)
    #Claves foráneas:
    producto_id = db.Column(db.Integer , db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer , db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)

#rutas
@app.route('/productos', methods = ['GET', 'POST'])
def nuevo_producto():
    form = ProductosForm()
    if form.validate_on_submit():
        #creamos un nuevo producto
        p = Producto(nombre = form.nombre.data, precio = form.precio.data)
        db.session.add(p)
        db.session.commit()
        return "Producto registrado"
    return render_template('nuevo_producto.html', form = form)
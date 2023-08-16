from flask import render_template
from . import products

#definir las rutas
@products.route('/create')
def crear_producto():
    return render_template('new.html')
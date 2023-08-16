#dependencia para hacer un Blueprint
from flask import Blueprint

#definir paquete 'products'
products = Blueprint(
    'products',
    __name__,
    url_prefix='/products',
    template_folder='templates')

from  . import routes
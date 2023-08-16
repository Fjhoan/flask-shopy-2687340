#dependencia de flask
from flask import Flask

#dependencia de configuración
#se llama al archivo que esta dentro de una carpeta con el . = .config
#el Config con C mayuscula, es el nombre de la clase
from .config import Config

#dependencia de modelos
from flask_sqlalchemy import SQLAlchemy

#dependencia de la migraciones
from flask_migrate import Migrate

#crear el objeto Flask
app = Flask(__name__)

#configuración del objeto Flask
app.config.from_object(Config)

#crear el objeto de los modelos
db = SQLAlchemy(app)

#crear el objeto de migración
migrate = Migrate(app, db)

#importar los modelos de .models
from .models import Cliente,Producto,Venta,Detalles
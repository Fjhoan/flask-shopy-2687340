class Config:
    #definir la 'cadena de conexión' (connection string) para el proyecto
    #Por fallas del equipo, se toco agregarle al mysql = +pymysql, quedando así 'mysql+pymysql://root:@localhost/flask-shopy-2687340'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin1234@localhost:3311/flask-shopy-2687340'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = 'ficha2687340'
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Importar las vistas
# from componentes.vistas_api import *
from componentes.vistas_web import *
from componentes.vistas_api_productos import *

# Lo siguiente sólo en desarrollo, no en producción
if __name__ == '__main__':
    app.run(debug=True)
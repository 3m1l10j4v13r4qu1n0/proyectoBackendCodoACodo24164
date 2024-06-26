#Vistas para la arquitectura API REST   
from flask import jsonify
from main import app
from componentes.modelo_tabla import Tabla
from servicios.prueba_back_json import tabla_completa

@app.route('/')
def home():
    print("estoy aca")
    return "tu usuario"
# error a querer poner mas de dos direcciones /api
# @app.route('/usuario_id')
# def mostrar_usuario_id():
#     t = tabla_completa
#     usuario = Tabla()
#     _datos = usuario.obtener_fila_id(t)
#     return jsonify(_datos)

@app.route('/api/tabla_usuario')
def mostrar_tabla_usuario():
    t1 = tabla_completa
    usuario = Tabla()
    _datos = usuario.obtener_tabla(t1)
    return jsonify(_datos)
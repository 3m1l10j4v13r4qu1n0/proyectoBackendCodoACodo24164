#Vistas para la arquitectura API REST   
from flask import jsonify
from main import app
from componentes.modelo_tabla import Tabla
from servicios.prueba_back_json import Ingreso_data
data = {
    "apellido": "aquino",
    "email": "correo@corre.com",
    "id": 7,
    "nombre": "emilio",
    "telefono": "125208147"
  }

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

@app.route('/api/usuarios')
def usurios():
    dato_l = Ingreso_data(data,tabla="usuario")
    dato = dato_l.crear_data()
    lista_usuarios = Tabla.obtener_tabla(dato)
    return jsonify(lista_usuarios)
#tira error si no se refresca el servidor
@app.route('/api/usuarios/usuario/<id>')
def user(id):
    dato_u = Ingreso_data(data,tabla="usuario")
    dato_u = dato_u.crear_data()
    usuario = Tabla.obtener_fila_id(str(id),dato_u)
    return jsonify(usuario)










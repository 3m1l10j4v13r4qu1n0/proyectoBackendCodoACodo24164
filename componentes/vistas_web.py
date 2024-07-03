# Importamos la función render_template de Flask para renderizar templates HTML.
from flask import Flask, render_template, request, redirect, session, jsonify
from conexion_db import config_db as c_db
from componentes.modelos import Data_login
# Importamos las funciones todos_los_productos y ver_producto desde el módulo modelo_producto.
from componentes.modelo_producto import todos_los_productos
from componentes.modelo_producto import ver_producto
from main import app
# Definimos una ruta para el endpoint raíz '/'.
# Esta función renderiza la plantilla 'inicio.html'.









@app.route('/',methods=['GET', 'POTS'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'userName'in request.form and 'userPassword':
        _userName = request.form['userName']
        _userPassword = request.form['userPassword']
        print(_userName)
        print(_userPassword)
        try:
            lista_login = Data_login().lista_data_login
        except TypeError:
            # Si el usuario no existe, devolver error 404 (No encontrado)
            return jsonify({'mensaje': 'login no encontrado'}), 404
        print(lista_login) 
        if _userName in lista_login[0]["userName"]:
            if   lista_login[0]["userPassword"] == _userName:
                return render_template('/base.html')
        else:
            return render_template('auth/login.html')

        

    return render_template('auth/login.html')


# Importamos la función render_template de Flask para renderizar templates HTML.
from flask import render_template
# Importamos la aplicación Flask (app) desde el archivo main.py.
from main import app
# Importamos las funciones todos_los_productos y ver_producto desde el módulo modelo_producto.
from componentes.modelo_producto import todos_los_productos
from componentes.modelo_producto import ver_producto
# Definimos una ruta para el endpoint raíz '/'.
# Esta función renderiza la plantilla 'inicio.html'.

@app.route('/')
def inicio():
    return render_template('inicio.html')
# Definimos una ruta para el endpoint '/inicio'.
# Esta función renderiza la plantilla 'inicio_auth.html'.
@app.route('/inicio')
def inicio_auth():
    return render_template('inicio_auth.html')
# Definimos una ruta para el endpoint '/api'.
# Esta función renderiza la plantilla 'api.html'.
@app.route('/api')
def api():
    return render_template('api.html')
# Definimos una ruta para el endpoint '/productos'.
# Esta función obtiene todos los productos llamando a la función todos_los_productos()
# y luego renderiza la plantilla 'productos.html', pasando los datos de los productos.
@app.route('/productos')
def productos():
    data = todos_los_productos()
    return render_template('productos.html', data=data)
# Definimos una ruta para el endpoint '/productos/nuevo'.
# Esta función renderiza la plantilla 'producto_nuevo.html'.
@app.route('/productos/nuevo')
def producto_nuevo():
    return render_template('producto_nuevo.html')
# Definimos una ruta para el endpoint '/productos/modificar/<string:id>'.
# Esta función recibe un parámetro 'id' que identifica el producto a modificar.
# Llama a la función ver_producto(id) para obtener los datos del producto
# y luego renderiza la plantilla 'producto_modificar.html', pasando los datos del producto
@app.route('/productos/modificar/<string:id>')
def producto_modificar(id):
    data = ver_producto(id)
    return render_template('producto_modificar.html', data=data)

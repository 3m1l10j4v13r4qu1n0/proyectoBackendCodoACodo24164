from main import app
from flask import jsonify
from flask import request
from flask import redirect
from flask import url_for


# from componentes.modelo_producto import Producto
from componentes.modelo_producto import crear_producto
from componentes.modelo_producto import todos_los_productos
from componentes.modelo_producto import eliminar_producto
from componentes.modelo_producto import editar_producto


#Mostar todos los productos
@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    data = todos_los_productos()
    return jsonify(data)

#Crear un producto
@app.route('/api/productos/nuevo', methods=['POST'])
def agregar_producto():
    if request.method == 'POST':
        titulo = request.form['titulo']
        imagen = request.form['imagen']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        crear_producto(titulo, imagen, descripcion, precio)
    return redirect(url_for('productos'))


#Elimar un producto
@app.route('/api/productos/eliminar/<string:id>')
def eliminar_un_producto(id):
    eliminar_producto(id)
    return redirect(url_for('productos'))

#Editar un producto
@app.route('/api/productos/editar/<string:id>', methods=['POST'])
def editar_un_producto(id):
    if request.method == 'POST':
        titulo = request.form['titulo']
        imagen = request.form['imagen']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        editar_producto(id, titulo, imagen, descripcion, precio)
    return redirect(url_for('productos'))
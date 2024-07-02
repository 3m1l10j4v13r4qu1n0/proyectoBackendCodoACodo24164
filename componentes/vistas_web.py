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
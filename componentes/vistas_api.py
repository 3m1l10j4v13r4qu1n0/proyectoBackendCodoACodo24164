#Vistas para la arquitectura API REST   
from componentes.modelos import User,Users
from servicios.prueba_back_json import Ingreso_data
from flask import  request, jsonify
from main import app



#Ruta para obtener todos los usuarios (GET)
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    try:
       usuarios = Users()
    except TypeError:
        # Si el usuario no existe, devolver error 404 (No encontrado)
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404 
    return jsonify(usuarios.__dict__["lista_user"])

#Ruta para crear un nuevo usuario (POST)
@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    # usuario_post = Tabla()
    # #Obtener datos del usuario del cuerpo de la solicitud
    # nuevo_usuario= request.get_json()
    # #Agregar el nuevo usuario a la lista
    # data_tabla_nuevo = Ingreso_data(tabla="usuario",nuevo_request=nuevo_usuario)
    # dato_nuevo = data_tabla_nuevo.crear_data()
    # usuario_post.agregar_fila(datos=dato_nuevo)
    # # Devolver respuesta con código de estado 201 (Creado)
    return jsonify({'mensaje': 'Usuario creado exitosamente'}), 201

#  # Ruta para eliminar un usuario existente (DELETE)
# @app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
# def eliminar_usuario(codigo):
#     # Buscar el usuario con el ID especificado
   
#     mensaje = codigo
#         #Tabla.eliminar_fila_id(str(id_usuario), datos={"tabla":"usuario"})
#         # Si el usuario no existe, devolver error 404 (No encontrado)
#         #return jsonify({'mensaje': 'Usuario no encontrado'}), 404
#     # # Eliminar el usuario de la lista
#     # Devolver respuesta con código de estado 200 (OK)
#     return jsonify({'mensaje': f'Usuario eliminado exitosamente el id:{mensaje}'})


#Ruta para obtener un usuario específico (GET)
@app.route('/api/usuarios/<int:id_usuario>', methods=['GET'])
def get_usuario(id_usuario):
    # Buscar el usuario con el ID especificado
    try:
        usuario = User(str(id_usuario))
    except TypeError:
        # Si el usuario no existe, devolver error 404 (No encontrado)
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404    
    # Devolver el usuario encontrado
    return jsonify(usuario.__dict__)

# Ruta para actualizar un usuario existente (PUT)
@app.route('/api/usuarios/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    # Buscar el usuario con el ID especificado
    nuevo_usuario= request.get_json()
    try:
        #Agregar el nuevo usuario a la lista
        User.actulizar_fila(str(id_usuario),datos=Ingreso_data.get_request(nuevo_request=nuevo_usuario))
    except TypeError:
        # Si el usuario no existe, devolver error 404 (No encontrado)
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404
    return jsonify("se actualizo el usuario correctamenta")

  












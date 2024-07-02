#Vistas para la arquitectura API REST   
from componentes.modelo_tabla import Tabla
from componentes.modelos import User
from servicios.prueba_back_json import Ingreso_data
from flask import  request, jsonify
from main import app


# def cargar_ram_usuarios(usuarios:list) -> list:
#     _users = []
#     data_tabla = Ingreso_data(data={},tabla="usuario")
#     dato = data_tabla.crear_data()
#     lista_usuarios = Tabla.obtener_tabla(datos=dato)
#     for i in range(len(lista_usuarios)):
#         _users.append(lista_usuarios[i])
#     return _users



 



# Lista de usuarios (inicialmente vacía)

#Ruta para obtener todos los usuarios (GET)
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    data_tabla = Ingreso_data(data={},tabla="usuario")
    dato = data_tabla.crear_data()
    lista_usuarios = Tabla.obtener_tabla(datos=dato)
    return jsonify(lista_usuarios)

#Ruta para crear un nuevo usuario (POST)
@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    usuario_post = Tabla()
    #Obtener datos del usuario del cuerpo de la solicitud
    nuevo_usuario= request.get_json()
    #Agregar el nuevo usuario a la lista
    agre=[]
    agre.append(nuevo_usuario)
    data_tabla_nuevo = Ingreso_data(data=agre[0],tabla="usuario")
    dato_nuevo = data_tabla_nuevo.crear_data()
    usuario_post.agregar_fila(datos=dato_nuevo)
    # Devolver respuesta con código de estado 201 (Creado)
    return jsonify({'mensaje': 'Usuario creado exitosamente'}), 201

#Ruta para obtener un usuario específico (GET)
@app.route('/api/usuarios/<int:id_usuario>', methods=['GET'])
def get_usuario(id_usuario):
    # Buscar el usuario con el ID especificado
    try:
        usuario_id_get = User(str(id_usuario))
    except TypeError:
        # Si el usuario no existe, devolver error 404 (No encontrado)
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404    
    # Devolver el usuario encontrado
    return jsonify(usuario_id_get.__dict__)

# Ruta para actualizar un usuario existente (PUT)
# @app.route('/api/usuarios/<int:id_usuario>', methods=['PUT'])
# def actualizar_usuario(id_usuario):
#     # Buscar el usuario con el ID especificado
#     usuario = [u for u in usuarios if u['id'] == id_usuario]

#     # Si el usuario no existe, devolver error 404 (No encontrado)
#     if not usuario:
#         return jsonify({'mensaje': 'Usuario no encontrado'}), 404

#     # Obtener datos actualizados del usuario del cuerpo de la solicitud
#     datos_actualizados = request.get_json()

#     # Actualizar el usuario con los nuevos datos
#     usuario[0].update(datos_actualizados)

#     # Devolver respuesta con código de estado 200 (OK)
#     return jsonify({'mensaje': 'Usuario actualizado exitosamente'})

# # Ruta para eliminar un usuario existente (DELETE)
# @app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
# def eliminar_usuario(id_usuario):
#     # Buscar el usuario con el ID especificado
#     usuario = [u for u in usuarios if u['id'] == id_usuario]

#     # Si el usuario no existe, devolver error 404 (No encontrado)
#     if not usuario:
#         return jsonify({'mensaje': 'Usuario no encontrado'}), 404

#     # Eliminar el usuario de la lista
#     usuarios.remove(usuario[0])

#     # Devolver respuesta con código de estado 200 (OK)
#     return jsonify({'mensaje': 'Usuario eliminado exitosamente'})











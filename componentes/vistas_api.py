#Vistas para la arquitectura API REST   
from flask import  request, jsonify
from main import app
data = {
    "apellido": "aquino",
    "email": "correo@corre.com",
    "id": 7,
    "nombre": "emilio",
    "telefono": "125208147"
  }

 



# Lista de usuarios (inicialmente vacía)
usuarios = [{
    "apellido": "aquino",
    "email": "correo@corre.com",
    "id": 7,
    "nombre": "emilio",
    "telefono": "125208147"
  },{
    "apellido": "perez",
    "email": "correo@corre.com",
    "id": 8,
    "nombre": "fabian",
    "telefono": "1123245678"
  }
]

# Ruta para obtener todos los usuarios (GET)
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

# Ruta para crear un nuevo usuario (POST)
@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    # Obtener datos del usuario del cuerpo de la solicitud
    nuevo_usuario = request.get_json()

    # Agregar el nuevo usuario a la lista
    usuarios.append(nuevo_usuario)

    # Devolver respuesta con código de estado 201 (Creado)
    return jsonify({'mensaje': 'Usuario creado exitosamente'}), 201

# Ruta para obtener un usuario específico (GET)
@app.route('/api/usuarios/<int:id_usuario>', methods=['GET'])
def get_usuario(id_usuario):
    # Buscar el usuario con el ID especificado
    usuario = [u for u in usuarios if u['id'] == id_usuario]

    # Si el usuario no existe, devolver error 404 (No encontrado)
    if not usuario:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    # Devolver el usuario encontrado
    return jsonify(usuario[0])

# Ruta para actualizar un usuario existente (PUT)
@app.route('/api/usuarios/<int:id_usuario>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    # Buscar el usuario con el ID especificado
    usuario = [u for u in usuarios if u['id'] == id_usuario]

    # Si el usuario no existe, devolver error 404 (No encontrado)
    if not usuario:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    # Obtener datos actualizados del usuario del cuerpo de la solicitud
    datos_actualizados = request.get_json()

    # Actualizar el usuario con los nuevos datos
    usuario[0].update(datos_actualizados)

    # Devolver respuesta con código de estado 200 (OK)
    return jsonify({'mensaje': 'Usuario actualizado exitosamente'})

# Ruta para eliminar un usuario existente (DELETE)
@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    # Buscar el usuario con el ID especificado
    usuario = [u for u in usuarios if u['id'] == id_usuario]

    # Si el usuario no existe, devolver error 404 (No encontrado)
    if not usuario:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

    # Eliminar el usuario de la lista
    usuarios.remove(usuario[0])

    # Devolver respuesta con código de estado 200 (OK)
    return jsonify({'mensaje': 'Usuario eliminado exitosamente'})











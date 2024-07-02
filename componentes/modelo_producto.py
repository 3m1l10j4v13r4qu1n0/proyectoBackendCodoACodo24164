from conexion_db import config_db


#Mostar todos los productos
def todos_los_productos():
        sql = config_db.conexion
        sql.connect()
        cursor = sql.cursor(dictionary=True)
        consulta = "SELECT * FROM producto;"
        cursor.execute(consulta)
        data = cursor.fetchall()
        sql.close()
        return data

#Crear un producto
def crear_producto(titulo, imagen, descripcion, precio):
    sql = config_db.conexion
    sql.connect()
    cursor = sql.cursor()
    consulta = "INSERT INTO producto (titulo, imagen, descripcion, precio) VALUES (%s, %s, %s, %s);"
    data = (titulo, imagen, descripcion, precio)
    cursor.execute(consulta, data)
    sql.commit()
    sql.close()

#Ver un producto
def ver_producto(id):
    sql = config_db.conexion
    sql.connect()
    cursor = sql.cursor(dictionary=True)
    consulta = f'SELECT * FROM producto WHERE id = {id}'
    cursor.execute(consulta)
    data = cursor.fetchall()
    sql.close()
    return data[0]

#Eliminar un producto
def eliminar_producto(id):
    sql = config_db.conexion
    sql.connect()
    cursor = sql.cursor()
    consulta = f"DELETE FROM producto WHERE id = {id};"
    cursor.execute(consulta)
    sql.commit()
    sql.close()

#Actulizar un producto
def editar_producto(id, titulo, imagen, descripcion, precio):
    sql = config_db.conexion
    sql.connect()
    cursor = sql.cursor()
    consulta = 'UPDATE producto SET titulo = %s, imagen = %s, descripcion = %s, precio = %s WHERE id = %s;'
    data = (titulo, imagen, descripcion, precio, id)
    cursor.execute(consulta, data)
    sql.commit()
    sql.close()
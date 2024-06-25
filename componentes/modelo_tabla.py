import config_db as c_db
from mysql.connector import Error



class Tabla:
    #atributos de clase
    _conexion = c_db.conexion
    
    
    def __init__(self):
       pass
    
    
    @classmethod
    def obtener_tabla(cls, datos:dict[str,str]) -> list[dict[str,str]]:
        if cls._conexion.is_connected():
            print(f'Inicio de conexion de tabla {datos["tabla"]}!')
            try:
                cls._conexion.connect()
                cursor = cls._conexion.cursor()
                consulta = f"SELECT * FROM {datos["tabla"]}"
                cursor.execute(consulta)
                columns = [column[0] for column in cursor.description]
                #print(columns)
                resultado = []
                for row in cursor.fetchall():
                    resultado.append(dict(zip(columns, row)))
                cls._conexion.close()
                print(resultado)
                return resultado
            except Error as ex:
                print(f'Error al intentar la conexión: {ex}')

    
    @classmethod
    def agregar_fila(cls,datos:dict[str,str]):
        if cls._conexion.is_connected():
            print(f'Inicio de conexion de tabla {datos["tabla"]}!')
            try:
                cls._conexion.connect()
                cursor = cls._conexion.cursor()
                consulta = f"INSERT INTO {datos["tabla"]} {str(datos["campos"]).replace("'", "`")} VALUES ({datos['comodin']});"
                dato = (datos["valores"])
                cursor.execute(consulta,dato )
                cls._conexion.commit()
                cls._conexion.close()
                print(f'se guardo correctamente en la tabla {datos["tabla"]}!')
            except Error as ex:
                print(f'Error al intentar la conexión: {ex}')

    @classmethod
    def obtener_fila_id(cls, datos:dict[str,str]) -> list[dict[str,str]]:
        if cls._conexion.is_connected():
            print(f'Inicio de conexion de tabla {datos["tabla"]}!')
            try:
                cls._conexion.connect()
                cursor = cls._conexion.cursor()
                consulta = F'SELECT * FROM {datos["tabla"]} WHERE id = {datos["comodin"]};'
                dato = (datos["valores"],)
                cursor.execute(consulta,dato)
                columns = [column[0] for column in cursor.description]
                #print(columns)
                resultado = []
                for row in cursor.fetchall():
                    resultado.append(dict(zip(columns, row)))
                #resultado = cursor.fetchone()
                cls._conexion.close()
                print(resultado)
                return resultado
            except Error as ex:
                print(f'Error al intentar la conexión: {ex}')
    
    def eliminar_fila_id(cls, datos:dict[str,str]):
        if cls._conexion.is_connected():
            print(f'Inicio de conexion de tabla {datos["tabla"]}!')
            try:
                cls._conexion.connect()
                cursor = cls._conexion.cursor()
                consulta = f"DELETE FROM {datos["tabla"]} WHERE id = {datos["comodin"]};"
                dato = (datos["valores"],)
                cursor.execute(consulta,dato)
                cls._conexion.commit()
                cls._conexion.close()
                print(f"¡Tabla {datos["tabla"]} elimino id = {datos["valores"]}!\n")
            except Error as ex:
                print(f'Error al intentar la conexión: {ex}')

usuario = Tabla()


datos = {
    "tabla": "usuario",
    "campos": (),
    "valores": (9),
    "comodin": f'%s'
}
datos1 = {
    "tabla": "usuario",
    "campos": ('nombre','apellido','email','telefono'),
    "valores": ("fabian","gonzales","correo@correo.com","1123453467"),
    "comodin": f'%s,%s,%s,%s'
}

da = {
    "tabla": "usuario",
    "campos": (),
    "valores": (6),
    "comodin": f'%s'
}

usuario.obtener_tabla(datos)
#usuario.obtener_fila_id(datos)


from conexion_db import config_db as c_db

class Tabla:
    #atributos de clase
    _conexion = c_db.conexion
    _error = c_db.error
    
    def __init__(self):
       pass
    
    @classmethod
    def obtener_tabla(cls, datos:dict[str, any]) -> list[dict[str, any]]:
        if cls._conexion.is_connected():
            print(f'Inicio de conexion de tabla {datos["tabla"]}!')
            try:
                cls._conexion.connect()
                cursor = cls._conexion.cursor()
                consulta = f"SELECT * FROM {f'{datos["tabla"]}'}"
                cursor.execute(consulta)
                columns = [column[0] for column in cursor.description]
                #print(columns)
                resultado = []
                for row in cursor.fetchall():
                    resultado.append(dict(zip(columns, row)))
                cls._conexion.close()
                print(resultado)
                return resultado
            except cls._error as ex:
                print(f'Error al intentar la conexión: {ex}')

    
    @classmethod
    def agregar_fila(cls,datos:dict[str, any]):
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
            except cls._error as ex:
                print(f'Error al intentar la conexión: {ex}')

    @classmethod
    def obtener_fila_id(cls, id:str, datos:dict[str, any]) -> list[dict[str, any]]:
        if cls._conexion.is_connected():
            print(f'Inicio de conexion de tabla {datos["tabla"]}!')
            try:
                cls._conexion.connect()
                cursor = cls._conexion.cursor()
                consulta = f'SELECT * FROM {datos["tabla"]} WHERE id = %s;'
                dato = (id,)
                cursor.execute(consulta,dato)
                columns = [column[0] for column in cursor.description]
                resultado = []
                for row in cursor.fetchall():
                    resultado.append(dict(zip(columns, row)))
                cls._conexion.close()
                print(resultado)
                return resultado
            except cls._error as ex:
                print(f'Error al intentar la conexión: {ex}')
    
    def eliminar_fila_id(cls, datos:dict[str, any]):
        if cls._conexion.is_connected():
            print(f'Inicio de conexion de tabla {datos["tabla"]}!')
            try:
                cls._conexion.connect()
                cursor = cls._conexion.cursor()
                consulta = f"DELETE FROM {datos["tabla"]} WHERE id = %s;"
                dato = (datos["id"],)
                cursor.execute(consulta,dato)
                cls._conexion.commit()
                cls._conexion.close()
                print(f"¡Tabla {datos["tabla"]} elimino id = {datos["id"]}!\n")
            except cls._error as ex:
                print(f'Error al intentar la conexión: {ex}')




#from conexion_db import config_db as c_db

class Tabla:
    #atributos de clase
    # _conexion = c_db.conexion
    # _error = c_db.error
    
    def __init__(self):
       pass
    
    def crear(self,d:dict[str, any]):
       for campo, valor in zip(d["campos"],d["valores"]):
           setattr(self, campo, valor)

    @classmethod
    def obtener_tabla(cls, datos:dict[str, any]) -> list[dict[str, any]]:
        consulta = f"SELECT * FROM {f'{datos["tabla"]}'}"
        return consulta
    
    
    
    @classmethod
    def obtener_fila_id(cls,datos:dict[str, any]) -> list[dict[str, any]]:
        consulta = f'SELECT * FROM {datos["tabla"]} WHERE id = %s;'
        return consulta
    
    @classmethod
    def agregar_fila(cls, datos:dict[str, any]):
        if cls._conexion.is_connected():
            #print(f'Inicio de conexion de tabla {datos["tabla"]}!')
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
    def actulizar_fila(cls, id:str, datos:dict[str, any]) -> list[dict[str, any]]:
        # try:
        #     cls._conexion.cursor()
        # except cls._error as ex:
        #     print(f'Error al intentar la conexión: {ex}')
        # cursor = cls._conexion.cursor()
        # consulta = f"UDDATE usuario SET {"nombre".replace("'", "`")} = %s WHERE id = %s;"
        # dato = (datos["nombre"],id,)
        # cursor.execute(consulta,dato )
        # cls._conexion.commit()
        # cls._conexion.close()
        if cls._conexion.is_connected():
            #print(f'Inicio de conexion de tabla {datos["tabla"]}!')
            try:
                cls._conexion.connect()
                cursor = cls._conexion.cursor()
                consulta = f"UPDATE usuario SET apellido = %s, nombre = %s, email = %s, telefono = %s WHERE id =%s;"
                dato = (datos["apellido"],datos["nombre"],datos["email"],datos["telefono"],id,)
                cursor.execute(consulta,dato)
                cls._conexion.commit()
                cls._conexion.close()
                print(f'se actualizo correctamente!')
            except cls._error as ex:
                print(f'Error al intentar la conexión: {ex}')
    
        

    
    @classmethod
    def eliminar_fila_id(cls,id,datos):
        if cls._conexion.is_connected():
            #print(f'Inicio de conexion de tabla {datos["tabla"]}!')
            try:
                cls._conexion.connect()
                cursor = cls._conexion.cursor()
                consulta = f"DELETE FROM {datos["tabla"]} WHERE id = %s;"
                dato = (id,)
                cursor.execute(consulta,dato)
                cls._conexion.commit()
                cls._conexion.close()
                print(f"¡Tabla {datos["tabla"]} elimino id = {id}!\n")
            except cls._error as ex:
                print(f'Error al intentar la conexión: {ex}')
        
            




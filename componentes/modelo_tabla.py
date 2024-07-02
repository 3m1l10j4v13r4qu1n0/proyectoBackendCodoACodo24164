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
        consulta = f"INSERT INTO {datos["tabla"]} {str(datos["campos"]).replace("'", "`")} VALUES ({datos['comodin']});"
        return consulta
    
    @classmethod
    def actulizar_fila(cls) -> list[dict[str, any]]:
        consulta = f"UPDATE usuario SET apellido = %s, nombre = %s, email = %s, telefono = %s WHERE id =%s;"
        return consulta
    
    @classmethod
    def eliminar_fila_id(cls,datos:dict[str, any]):
        consulta = f"DELETE FROM {datos["tabla"]} WHERE id = %s;"
        return consulta    




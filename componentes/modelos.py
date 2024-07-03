from servicios.prueba_back_json import Ingreso_data
from componentes.modelo_tabla import Tabla
from conexion_db.modelo_conexion import Conexion_tabla
from conexion_db import config_db as c_db

class User(Tabla):
    datos = {"tabla":"usuario"}
    _cox = Conexion_tabla(cox= c_db.conexion, consulta=Tabla.obtener_fila_id(datos= datos))
    def __init__(self,id:str="") -> dict[str, any]:
        super().crear(self._cox.obtener_fila_id(id)[0])
    




class Users:
    _cox = Conexion_tabla(cox= c_db.conexion, consulta=Tabla.obtener_tabla(datos={"tabla":"usuario"}))
    def __init__(self) -> None:
        self.lista_user = self._cox.obtener_tabla()

#### modelo datalogin  ####

class Data_login:
    _cox = Conexion_tabla(cox= c_db.conexion, consulta=Tabla.obtener_tabla(datos={"tabla":"datalogin"}))
    def __init__(self) -> None:
        self.lista_data_login = self._cox.obtener_tabla()

class User_dl(Tabla):
    datos = {"tabla":"datalogin"}
    _cox = Conexion_tabla(cox= c_db.conexion, consulta=Tabla.obtener_fila_id(datos= datos))
    def __init__(self,id:str="") -> dict[str, any]:
        super().crear(self._cox.obtener_fila_id(id)[0])


   
    
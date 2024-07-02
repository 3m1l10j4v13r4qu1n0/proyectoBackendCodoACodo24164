from conexion_db.modelo_conexion import Conexion_tabla
from conexion_db import config_db as c_db
from componentes.modelo_tabla import Tabla
cox = Conexion_tabla(cox= c_db.conexion, consulta=Tabla.obtener_tabla(datos={"tabla":"usuario"}))
lista = cox.obtener_tabla()
print(lista)
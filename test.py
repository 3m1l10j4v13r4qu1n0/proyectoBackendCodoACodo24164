from componentes.modelo_tabla import Tabla
from componentes.modelos import User
from componentes.modelos import User
from servicios.prueba_back_json import Ingreso_data
data = {
    "apellido": "rout",
    "email": "correo@corre.com",
    "id": None,
    "nombre": "carlos",
    "telefono": "1122333544"
  }
data_tabla = Ingreso_data(data,tabla="usuario")
dato = data_tabla.crear_data()
# usuario = Tabla()
# usuario.obtener_fila_id(id="13",datos= dato)
u = User(id="17").agregar_fila(datos=dato)

#print(usuario.__dict__)
print("*************************************")
# print(u.__dict__)





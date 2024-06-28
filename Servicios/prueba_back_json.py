data = {
    "apellido": "aquino",
    "email": "correo@corre.com",
    "id": 7,
    "nombre": "emilio",
    "telefono": "125208147"
  }

class Ingreso_data:
	def __init__(self,data:dict[str,any],tabla:str) -> dict[str,any]:
		self._tabla = tabla
		self._data = data
		self.campos= []
		self.valores=[]
		#self.comodin = self.agregar_comodin()
		for clave, valor in self._data.items():
			if clave != "id":
				self.campos.append(clave)
				self.valores.append(valor)
		def agregar_comodin(campos) -> str:
			index = '%s,'*len(campos)
			comodin = index[:-1]
			return comodin
		self.comodin = agregar_comodin(self.campos)

	def crear_data(self) -> dict[str,any]:
		data = {
			'tabla':self._tabla,
			'id':self._data["id"],
			'campos':(*self.campos,),
			'valores':(*self.valores,),
			'comodin': self.comodin
		}
		return data

#data_tabla = Ingreso_data(data,tabla="usuario")
#dato =data_tabla.crear_data()


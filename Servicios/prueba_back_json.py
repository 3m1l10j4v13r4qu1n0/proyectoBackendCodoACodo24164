

class Ingreso_data:
	
	def __init__(self,tabla:str,nuevo_request) -> dict[str,any]:
		self.tabla = tabla
		self.data = self.get_request(nuevo_request)
		self.campos= []
		self.valores=[]
		#self.id = ""
		#self.comodin = self.agregar_comodin()
		for clave, valor in self.data.items():
			if clave != "id":
				self.campos.append(clave)
				self.valores.append(valor)
			else:
				print("no se agrega id")
				#self.id = str(valor)
				

		def agregar_comodin(campos) -> str:
			index = '%s,'*len(campos)
			comodin = index[:-1]
			return comodin
		self.comodin = agregar_comodin(self.campos)

	def crear_data(self) -> dict[str,any]:
		data = {
			'tabla':self.tabla,
			'campos':(*self.campos,),
			'valores':(*self.valores,),
			'comodin': self.comodin
		}
		return data
	@classmethod
	def get_request(cls,nuevo_request):
		agre= {}
		agre.update(nuevo_request)
		return agre
		


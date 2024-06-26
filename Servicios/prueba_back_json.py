data = {
    "apellido": "smitch",
    "email": "correo@corre.com",
    "nombre": "sevastian",
    "telefono": "1123456789"
}



def ingreso_data(data:dict[str,any]) -> dict[str,any]:
	campos=[]
	valores=[]
	for clave, valor in data.items():
		campos.append(clave)
		valores.append(valor)
		
	return (campos),(valores)
		
		
def agregar_comodin(campos:tuple) -> str:
	
	index = '%s,'*len(campos)
	comodin = index[:-1]
	return comodin


def crear_data(tabla:str,id:int,campos:tuple,valores:tuple,comodin:str) -> dict[str,any]:
	data = {
	    'tabla':tabla,
		'id':(id),
	    'campos':(*campos,),
	    'valores':(*valores,),
	    'comodin': comodin
	}
	return data


i = ingreso_data(data)
c = agregar_comodin(i[0])
tabla = 'usuario'
id = 8
campos = i[0]
valores = i[1]
comodin = c
tabla_completa = crear_data(tabla,id,campos,valores,comodin)


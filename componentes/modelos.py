from componentes.modelo_tabla import Tabla

class User(Tabla):
    def __init__(self,id:str,nom_tabla={"tabla":"usuario"}):
        super().crear(self.obtener_fila_id(id,nom_tabla))



        
        
   
    
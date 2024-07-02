class Conexion_tabla:
    def __init__(self,cox,consulta):
        self._cox = cox
        self.consulta = consulta
    
    def crear(self,d:dict[str, any]):
       for campo, valor in zip(d["campos"],d["valores"]):
           setattr(self, campo, valor)
    
    def obtener_tabla(self):
        try:
            self._cox.connect()
        except Exception as ex:
            print(f'Error al intentar la conexión: {ex}')
        self._cox.connect()
        cursor = self._cox.cursor()
        cursor.execute(self.consulta)
        columns = [column[0] for column in cursor.description]
        #print(columns)
        resultado = []
        for row in cursor.fetchall():
            resultado.append(dict(zip(columns, row)))

        self._cox.close()
        #print(resultado)
        return resultado
    
    def obtener_fila_id(self,id):
      try:
          self._cox.connect()
      except Exception as ex:
          print(f'Error al intentar la conexión: {ex}')
      cursor = self._cox.cursor()
      dato = (id,)
      cursor.execute(self.consulta,dato)
      campos = [column[0] for column in cursor.description]
      valores = cursor.fetchone()
      resultado = []
      resultado.append(dict((("campos",campos),("valores",valores))))
      self._cox.close()
      return resultado
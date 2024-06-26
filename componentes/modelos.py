

        















# datos = {
#     "tabla": "usuario",
#     "campos": (),
#     "valores": (9),
#     "comodin": f'%s'
# }
# datos1 = {
#     "tabla": "usuario",
#     "campos": ('nombre','apellido','email','telefono'),
#     "valores": ("fabian","gonzales","correo@correo.com","1123453467"),
#     "comodin": f'%s,%s,%s,%s'
# }

# da = {
#     "tabla": "usuario",
#     "campos": (),
#     "valores": (6),
#     "comodin": f'%s'
# }
usuario = Tabla_factory(datos,Tabla())
usuario.saludar()
print(usuario)


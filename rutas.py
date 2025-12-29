#rutas de acceso a cada recurso
from recursos import *

#tener el objeto api
def crear_rutas(api):
    # quiero que puedas acceder a este recurso por medio de tal ruta
    # 1.el recurso que va a ejecutar - invocar
    # 2.la direccion de este recurso
    api.add_resource(hello_world, '/hello')

    # la ruta de inicio
    api.add_resource(PantallaInicio, '/')

    api.add_resource(Despedida, '/despedida')

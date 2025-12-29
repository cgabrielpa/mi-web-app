from flask_restful import Resource

from flask import make_response, render_template
#recursos que mi servidor tendra disponible
#vamos a crear recursos :_ para nosotros poder crear
# recursos lo haremos atravez de clases y objetos

class hello_world(Resource):
    def get(self): #los recursos van a poder ejecutar dos acciones -> metodos
        return {'hello': 'world'}

class PantallaInicio(Resource):
    def get(self):

        #renderizamos el contenido del archivo html
        contenido = render_template('index.html')
#retornamos el contenido renderizado en una respuesta
        return make_response(contenido)

class Despedida(Resource):
    def get(self):
        return 'Adios'
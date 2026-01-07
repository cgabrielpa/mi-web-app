from flask_restful import Resource

from flask import make_response, render_template, request
#recursos que mi servidor tendra disponible
#vamos a crear recursos :_ para nosotros poder crear
# recursos lo haremos atravez de clases y objetos
from extensiones import inicializar_db

cliente = inicializar_db()


class PantallaInicio(Resource):
    def get(self):

        #renderizamos el contenido del archivo html
        contenido = render_template('index.html')
#retornamos el contenido renderizado en una respuesta
        return make_response(contenido)

class Despedida(Resource):
    def get(self):
        return 'Adios'

class Login(Resource):
    def get(self):
        contenido = render_template('login.html')
        return make_response(contenido)

    #no tenemos la manera de soportar un post

    def post(self):
        print('Esto se ejecuta cuando se llama a un post')

        datos = request.form.to_dict()

        print(datos)

        contenido = render_template('SeccionIniciada.html')

        if datos['password']=='hola123' and datos['correo']=='gabriel@hola.com':
            return make_response(contenido)
        else:
            return 'Datos incorrectos'

class CrearCuenta(Resource):
    def get(self): #los recursos van a poder ejecutar dos acciones -> metodos
        contenido = render_template('crearcuenta.html')
        return make_response(contenido)

    def post(self):

        datos = request.form.to_dict()
        print(datos)

        cliente.table('usuarios').insert(datos).execute()

        #esto va guardar la informacion en la tabla usuarios de supabase
        return 'Correcto:D'

class SeccionIniciada(Resource):
    def get(self):
        contenido = render_template('SeccionIniciada.html')
        return make_response(contenido)
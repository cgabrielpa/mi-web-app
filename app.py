from flask import Flask, make_response, redirect, render_template, request

#Desde flask_restful importamos la clase api y la clase resource
from flask_restful import Api, Resource
from rutas import crear_rutas

app = Flask(__name__)#creamos un objeto de tipo flask
#creamos un objeto de tipo Api y como argumento le pasamos el objeto app
#el parametro/argumento que espera recibir es el objeto de flask
api = Api(app)
#la api sera el rpopgrama que se comunique con el dispositivo fisico

crear_rutas(api)

if __name__ == '__main__':
    app.run()

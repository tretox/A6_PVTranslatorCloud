'''
Created on Dec 6, 2018

@author: Carlos
'''

from google.appengine.ext import db
from datetime import datetime

class Modules(db.Model):
    name = db.StringProperty()
    alpha = db.IntegerProperty()
    beta = db.IntegerProperty()
    gamma = db.IntegerProperty()
    kappa = db.IntegerProperty()


class Campanyas(db.Model):
    name = db.StringProperty()
    modulo = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
    
class Meteo:
    def __init__(self, tiempo, temperatura, humedad, velocidadViento, direccionViento, nubesActual, fecha):
        self.tiempo = tiempo
        self.temperatura = temperatura
        self.humedad = humedad
        self.velocidadViento = velocidadViento
        self.direccionViento = direccionViento
        self.nubesActual = nubesActual
        self.fecha = fecha
    

class Comments(db.Model):
    text = db.StringProperty(multiline=True)
    createDate = db.DateTimeProperty(auto_now_add=True)
    updateDate = db.DateTimeProperty(auto_now_add=True)
    userName = db.StringProperty()
    userMail = db.StringProperty()
    campanya = db.StringProperty()
    module = db.StringProperty()
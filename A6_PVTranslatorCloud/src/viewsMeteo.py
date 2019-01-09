'''
Created on 1 ene. 2019

@author: Rafa
'''
from BaseHandler import BaseHandler
from models import Meteo
import json
import urllib2
import webapp2

apiKey = "07819c466ef342e6a4e5b9dbc8e7eb8e"
weatherCity = "Malaga,es"
units = "metric"
BASE_URI = "https://api.openweathermap.org/data/2.5/forecast?q=" + weatherCity + "&units=" + units + "&appid=" + apiKey
listaMeteo = []

class showVerTiempo(BaseHandler):
    
    def get(self, posicion):  
        global listaMeteo
        pos=int(posicion)
        if(listaMeteo==[]):
            req = urllib2.Request(BASE_URI)
            opener = urllib2.build_opener()
            respuesta = opener.open(req)
            jsonRespuesta = json.loads(respuesta.read())
            ja = jsonRespuesta["list"]
            for i in xrange(0,len(ja)):
                aux = ja[i]
    
                #//Tiempo actual//
                jaAux = aux["weather"]
                aux2 = jaAux[0]
                tiempo = aux2["description"]
                    
                #//TemperaturaActual//
                main = aux["main"]
                temperatura = main["temp"]
                #//HumedadActual//
                humedad = main["humidity"]
                    
                #//VelocidadVientoActual//
                wind = aux["wind"]
                velocidadViento = wind["speed"]
    
                #//DireccionVientoActual//
                direccionViento = wind["deg"]
                    
                #//NubesActual//
                clouds = aux["clouds"]
                nubesActual = clouds["all"]
                    
                #//FechaActual//
                fecha = aux["dt_txt"]
                    
                m = Meteo(tiempo, temperatura, humedad, velocidadViento, direccionViento, nubesActual, fecha)
                listaMeteo.append(m)

        listaMeteoDiv10 = self.crearListaMeteoDiv10(pos)
        self.render_template('verTiempo.html', { 
            "ListaTiempo" : listaMeteoDiv10, 
            "renderizarNext" : self.renderizarNext(pos), 
            "renderizarBack":self.renderizarBack(pos), 
            "weatherCity":weatherCity,
            "posicion":pos
            })
        
    def crearListaMeteoDiv10(self, posicion) :
        pos=int(posicion)
        listaMeteoDiv10 = []
        if(len(listaMeteo)<pos*10+10):
            listaMeteoDiv10 = listaMeteo[pos*10 : len(listaMeteo)]
        else:
            listaMeteoDiv10 = listaMeteo[pos*10 : pos*10+10]
        return listaMeteoDiv10   
    
    def renderizarNext(self, posicion):
        pos=int(posicion)
        if(((pos+1)*10)>=len(listaMeteo)):
            return False
        else:
            return True
    
    def renderizarBack(self, posicion):
        pos=int(posicion)
        if(((pos-1)*10)<0):
            return False
        else:
            return True
    
class meteoNext(BaseHandler):
    def get(self, posicion):
        pos=int(posicion)
        if(((pos+1)*10)<len(listaMeteo)):
            pos=pos+1
        return webapp2.redirect('/verTiempo/'+str(pos))
    
class meteoBack(BaseHandler):
    def get(self, posicion):
        pos=int(posicion)
        if(((pos-1)*10)>=0):
            pos=pos-1
        return webapp2.redirect('/verTiempo/'+str(pos))
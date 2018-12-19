'''
Created on Dec 11, 2018

@author: Carlos
'''

import webapp2
import time

from BaseHandler import BaseHandler
from google.appengine.ext import db

from models import Campanyas
from datetime import datetime
from google.appengine.datastore.datastore_v4_pb import GqlQuery

class ShowCampanyas(BaseHandler):
    
    def get(self, id_modulo):
        

        campanyas=Campanyas.all().filter('modulo', int(id_modulo))
       
        self.render_template('campanya.html', {"campanyas" : campanyas,"id_modulo" : id_modulo})

        
class DeleteCampanya(BaseHandler):
    
    def get(self,id_campanya,id_modulo):
       
        idCampanya = int(id_campanya)
        #idModulo= int(id_modulo)
        campanya = db.get(db.Key.from_path('Campanyas', idCampanya))
        db.delete(campanya)
        time.sleep(0.1)
       
        return webapp2.redirect('/campanyas/'+id_modulo)
       
        
        
    
class NewCampaign(BaseHandler):

    def get(self, camp_id):
        if not camp_id:             #no hay campanya seleccionada
            self.render_template('newCampanya.html', {})
        else:
            id = int(camp_id)
            campanya = db.get(db.Key.from_path('Campanyas', id))
            self.render_template('newCampanya.html', {"campanya": campanya})
        
        
    def post(self, camp_id):
        campanya = None
        if not camp_id:             #no hay campanya seleccionada
            campanya = Campanyas(name=self.request.get('inputName'),
                         modulo=int("3"),)
        else:
            id = int(camp_id)
            campanya = db.get(db.Key.from_path('Campanyas', id))
            campanya.name = self.request.get('inputName')
            campanya.date = datetime.now()

        campanya.put()
        time.sleep(0.1) 
        return webapp2.redirect('/')

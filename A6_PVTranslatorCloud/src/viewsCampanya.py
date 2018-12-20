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

class ShowCampanyas(BaseHandler):
    
    def get(self, id_modulo):
        campanyas=Campanyas.all().filter('modulo', int(id_modulo))
        self.render_template('campanya.html', {"campanyas" : campanyas,"id_modulo" : id_modulo})

        
class DeleteCampanya(BaseHandler):
    
    def get(self,id_campanya,id_modulo):
       
        idCampanya = int(id_campanya)
        
        campanya = db.get(db.Key.from_path('Campanyas', idCampanya))
        db.delete(campanya)
        time.sleep(0.1)
       
        return webapp2.redirect('/campanyas/'+id_modulo)
       
        
        
    
class NewCampaign(BaseHandler):

    def get(self,id_modulo):
        self.render_template('newCampanya.html', {"id_modulo" : id_modulo})
        
    def post(self,id_modulo):
        campanya = None
        campanya = Campanyas(name=self.request.get('inputName'),modulo=int(id_modulo),)
        
        campanya.put()
        time.sleep(0.1) 
        return webapp2.redirect('/campanyas/'+id_modulo)

class EditCampaign(BaseHandler):

    def get(self, camp_id, id_modulo):
        id = int(camp_id)
        campanya = db.get(db.Key.from_path('Campanyas', id))
        self.render_template('newCampanya.html', {"campanya": campanya,"id_modulo" : id_modulo})
        
        
    def post(self, camp_id, id_modulo):
        campanya = None
        id = int(camp_id)
        campanya = db.get(db.Key.from_path('Campanyas', id))
        campanya.name = self.request.get('inputName')
        campanya.date = datetime.now()

        campanya.put()
        time.sleep(0.1) 
        return webapp2.redirect('/campanyas/'+id_modulo)


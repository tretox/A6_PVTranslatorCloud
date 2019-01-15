'''
Created on Dec 11, 2018

@author: Carlos
'''

import webapp2
#import time

from BaseHandler import BaseHandler
from google.appengine.ext import db

from models import Campanyas
from models import Modules
from datetime import datetime
from google.appengine.api import users


class ShowCampanyas(BaseHandler):
    
    def get(self, id_modulo):
        campanyas=Campanyas.all().filter('modulo', int(id_modulo))
        module = Modules.get(db.Key.from_path('Modules', int(id_modulo)))
        
        self.render_template('campanya.html', {"campanyas" : campanyas, "module" : module, "user" : users.get_current_user(), "admin" : users.is_current_user_admin()})

        
class DeleteCampanya(BaseHandler):
    
    def get(self,id_campanya):
       
        if users.is_current_user_admin():
            idCampanya = int(id_campanya)
            campanya = db.get(db.Key.from_path('Campanyas', idCampanya))
            id_mod = str(campanya.modulo)
            db.delete(campanya)
        
        #time.sleep(0.1)
        return webapp2.redirect('/campanyas/'+id_mod)
       
        
        
    
class NewCampaign(BaseHandler):

    def get(self,id_modulo):
        if users.is_current_user_admin():
            self.render_template('newCampanya.html', {"id_modulo" : id_modulo})
        else:
            return webapp2.redirect('/campanyas/'+id_modulo)
        
    def post(self,id_modulo):
        campanya = Campanyas(name=self.request.get('inputName'),modulo=int(id_modulo),)
        
        campanya.put()
        #time.sleep(0.1) 
        
        return webapp2.redirect('/campanyas/'+id_modulo)

class EditCampaign(BaseHandler):

    def get(self, camp_id):
        id = int(camp_id)
        campanya = db.get(db.Key.from_path('Campanyas', id))
            
        if users.is_current_user_admin():
            self.render_template('newCampanya.html', {"campanya": campanya,"id_modulo" : campanya.modulo})
        else:
            return webapp2.redirect('/campanyas/'+campanya.modulo)
        
    def post(self, camp_id):
        campanya = db.get(db.Key.from_path('Campanyas', int(camp_id)))
        campanya.name = self.request.get('inputName')
        campanya.date = datetime.now()

        campanya.put()
        #time.sleep(0.1) 
        return webapp2.redirect('/campanyas/'+str(campanya.modulo))


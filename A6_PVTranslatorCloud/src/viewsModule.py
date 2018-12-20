'''
Created on Dec 6, 2018

@author: Carlos
'''

import webapp2
import time

from BaseHandler import BaseHandler
from google.appengine.ext import db
from google.appengine.api import users
from models import Modules 


class ShowModules(BaseHandler):
    def get(self):
        modules = Modules.all()
        self.render_template('modules.html', {"modules": modules, "user" : users.get_current_user(), "admin" : users.is_current_user_admin()})
         
            
class LogIn(BaseHandler):
    def get(self):
        self.redirect(users.create_login_url('/'))


class LogOut(BaseHandler):
    def get(self):
        self.redirect(users.create_logout_url('/'))
        
        
class showCalendar(BaseHandler):
    
    def get(self):
        self.render_template('calendar.html', {})
        
        
class DeleteModulo(BaseHandler):
    
    def get(self, mod_id):
        id = int(mod_id)
        modulo = db.get(db.Key.from_path('Modules', id))
        db.delete(modulo)
        time.sleep(0.1)
        return webapp2.redirect('/')
        
        
class EditModule(BaseHandler):

    def get(self, mod_id):
        id = int(mod_id)
        modulo = db.get(db.Key.from_path('Modules', id))
        self.render_template('newEditModule.html', {"modulo": modulo})
        
    def post(self, mod_id):
        id = int(mod_id)
        module = db.get(db.Key.from_path('Modules', id))
        module.name = self.request.get('inputName')
        module.alpha = int(self.request.get('inputAlpha'))
        module.beta = int(self.request.get('inputBeta'))
        module.gamma = int(self.request.get('inputGamma'))
        module.kappa = int(self.request.get('inputKappa'))

        module.put()
        time.sleep(0.1) #Buscar otra sol.
        return webapp2.redirect('/')


class NewModule(BaseHandler):
    def get(self):
        self.render_template('newEditModule.html', {})
        
    def post(self):
        module = Modules(name=self.request.get('inputName'),
                         alpha=int(self.request.get('inputAlpha')),
                         beta=int(self.request.get('inputBeta')),
                         gamma=int(self.request.get('inputGamma')),
                         kappa=int(self.request.get('inputKappa')),)
        module.put()
        time.sleep(0.1) #Buscar otra sol.
        return webapp2.redirect('/')
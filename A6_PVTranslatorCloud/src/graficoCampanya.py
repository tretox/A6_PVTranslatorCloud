'''
Created on 12 ene. 2019

@author: alber
'''

import webapp2
import time
import json

from BaseHandler import BaseHandler
from google.appengine.ext import db
from google.appengine.api import users

from models import Comments

class ShowGraph(BaseHandler):
    
    def get(self, id_campanya):
       
        if users.is_current_user_admin():
            
        
            q = Comments.all()
            q.filter('campanya', id_campanya)
        
            listaEmail = []
            listaNumero = []
        
            x=0
            
            for c in q:
                if c.userMail in listaEmail:
                    listaNumero[listaEmail.index(c.userMail)]=listaNumero[listaEmail.index(c.userMail)]+1
                else:
                    listaEmail.insert(x, c.userMail)
                    listaNumero.insert(x,1)
                    x=x+1
                
             
             
                
            self.render_template('grafico.html', {"users" : listaEmail , "numeros" : listaNumero , "tam": len(listaEmail) })
        
        else:
            return webapp2.redirect('/') 
       
        

    
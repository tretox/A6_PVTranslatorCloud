'''
Created on Dec 6, 2018

@author: Carlos
'''

from google.appengine.ext import db

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
    
"""    
class Coments(db.model):
    text = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    userName = db.StringProperty()
    userMail = db.StringProperty() #String o del tipo que la clase User de google devuelva el correo

"""   
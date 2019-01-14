'''
Created on Dec 6, 2018

@author: Carlos
'''


from viewsCampanya import NewCampaign, ShowCampanyas, DeleteCampanya, EditCampaign
from viewsModule import ShowModules, LogIn, LogOut, NewModule, EditModule, showCalendar, DeleteModulo
from viewsMeteo import showVerTiempo, meteoBack, meteoNext
from viewsForo import ViewComments, NewComments, RemoveComments, EditComments
from graficoCampanya import ShowGraph

import webapp2

app = webapp2.WSGIApplication([
        ('/', ShowModules), 
        ('/login', LogIn), 
        ('/logout', LogOut), 
        
        ('/module/new', NewModule), 
        ('/module/edit/([\d]+)', EditModule), 
        ('/module/delete/([\d]+)', DeleteModulo),
        
        ('/calendar', showCalendar),
        ('/verTiempo/([\d]+)', showVerTiempo),
        ('/meteoBack/([\d]+)', meteoBack),
        ('/meteoNext/([\d]+)', meteoNext),
        
        ('/campanyas/([\d]+)', ShowCampanyas),
        ('/campanyas/new/([\d]+)', NewCampaign),           
        ('/campanyas/edit/([\d]+)', EditCampaign),    
        ('/campanyas/delete/(\d+)', DeleteCampanya),

        ('/foro/(\d+)/(\w+)', ViewComments),
        ('/foro/(\d+)/(\w+)/new', NewComments),
        ('/foro/(\d+)/(\w+)/remove', RemoveComments),
        ('/foro/(\d+)/(\w+)/edit', EditComments),
        
        ('/grafico/(\w+)',ShowGraph)
        ],
        debug=True)

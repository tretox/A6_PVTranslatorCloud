'''
Created on Dec 6, 2018

@author: Carlos
'''


from viewsCampanya import NewCampaign, ShowCampanyas, DeleteCampanya
from viewsModule import ShowModules, NewModule, EditModule, showCalendar, DeleteModulo

import webapp2  

app = webapp2.WSGIApplication([
        ('/', ShowModules), 
        ('/module/new', NewModule), 
        ('/module/edit/([\d]+)', EditModule), 
        ('/module/delete/([\d]+)', DeleteModulo),
        
        ('/calendar', showCalendar),
        
        ('/newCampaign/([\d]*)', NewCampaign),
        ('/campanyas/([\d]+)', ShowCampanyas),
        ('/deleteCampanya/(\d+);(\d+)', DeleteCampanya),
        ],
        debug=True)

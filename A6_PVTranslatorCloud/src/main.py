'''
Created on Dec 6, 2018

@author: Carlos
'''


from viewsCampanya import NewCampaign, ShowCampanyas, DeleteCampanya
from viewsModule import ShowModules, NewEditModule, showCalendar, DeleteModulo

import webapp2  

app = webapp2.WSGIApplication([
        ('/', ShowModules), 
        ('/newEditModule/([\d]*)', NewEditModule), 
        ('/calendar', showCalendar),
        ('/newCampaign/([\d]*)', NewCampaign),
        ('/campanyas/([\d]+)', ShowCampanyas),
        ('/deleteCampanya/(\d+);(\d+)', DeleteCampanya),
        ('/deleteModulo/([\d]+)', DeleteModulo),
        ],
        debug=True)

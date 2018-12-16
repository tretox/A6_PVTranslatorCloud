'''
Created on Dec 6, 2018

@author: Carlos
'''

from viewsModule import ShowModules, NewModule, showCalendar
from viewsCampanya import NewCampaign
import webapp2  

app = webapp2.WSGIApplication([
        ('/', ShowModules), 
        ('/newModule/([\d]*)', NewModule), 
        ('/calendar', showCalendar),
        ('/newCampaign/([\d]*)', NewCampaign),
        ],
        debug=True)

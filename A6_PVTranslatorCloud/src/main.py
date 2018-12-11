'''
Created on Dec 6, 2018

@author: Carlos
'''

from viewsModule import ShowModules, NewModule, showCalendar
import webapp2  

app = webapp2.WSGIApplication([
        ('/', ShowModules), 
        ('/newModule/([\d]*)', NewModule), 
        ('/calendar', showCalendar),
        ],
        debug=True)

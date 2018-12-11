'''
Created on Dec 6, 2018

@author: Carlos
'''

from viewsModule import ShowModules, NewEditModule, showCalendar, DeleteModulo
import webapp2  

app = webapp2.WSGIApplication([
        ('/', ShowModules), 
        ('/newEditModule/([\d]*)', NewEditModule), 
        ('/calendar', showCalendar),
        ('/deleteModulo/([\d]+)', DeleteModulo),
        ],
        debug=True)

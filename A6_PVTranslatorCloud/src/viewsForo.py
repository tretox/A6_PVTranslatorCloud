
import webapp2

import time
from datetime import datetime
from google.appengine.api import users
from google.appengine.ext import db
from models import Comments
from BaseHandler import BaseHandler

class ViewComments(BaseHandler):

    def get(self,module_id,campain_id):
        comments = Comments.all().filter('module = ', module_id).filter('campanya = ', campain_id).order('-createDate')
        self.render_template("foro.html", {
            "module" : module_id,
            "campain" : campain_id,
            "comments" : comments,
            "user" : users.get_current_user().nickname() if users.get_current_user() != None else None,
            "admin" : users.is_current_user_admin()}
        )

class NewComments(ViewComments):

    def post(self, module_id, campain_id):
        text = self.request.get("comment")
        user = users.get_current_user()

        comment = Comments(
            text=text.strip(),
            userMail=user.email(),
            userName=user.nickname(),
            campanya=campain_id,
            module=module_id
        )

        comment.put()
        return webapp2.redirect("/foro/"+str(module_id)+"/"+str(campain_id))

class RemoveComments(NewComments):

    def post(self, module_id, campain_id):
        date = self.request.get("date")
        user = self.request.get("user")

        dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')

        q = Comments.all();
        q = q.filter('userMail = ', user)
        q = q.filter('module = ', module_id)
        q = q.filter('campanya = ', campain_id)
        q = q.filter('createDate = ', dt)

        comment = q.fetch(1)
        db.delete(comment)

        return webapp2.redirect("/foro/"+str(module_id)+"/"+str(campain_id))

class EditComments(NewComments):

    def post(self, module_id, campain_id):
        date = self.request.get("date")
        user = self.request.get("user")
        text = self.request.get("text")

        dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')

        q = Comments.all()
        q = q.filter('userMail = ', user)
        q = q.filter('module = ', module_id)
        q = q.filter('campanya = ', campain_id)
        q = q.filter('createDate = ', dt)

        comment = q.fetch(1)
        comment[0].text = text
        comment[0].updateDate = datetime.now()
        db.put(comment)

        return

"""
class Comments(db.Model):
    text = db.StringProperty()
    createDate = db.DateTimeProperty(auto_now_add=True)
    updateDate = db.DateTimeProperty(auto_now_add=True)
    userName = db.StringProperty()
    userMail = db.StringProperty()
    campanya = db.StringProperty()
    module = db.StringProperty()
"""
import webapp2
import jinja2
import os
import cgi

from models import Navigation
import config
import structure

from google.appengine.api import users
from google.appengine.ext import db

class MainPage(webapp2.RequestHandler):
    def get(self):
        navigation_query = Navigation.all().order('order')

        user = users.get_current_user()
        navigation = navigation_query.fetch(10)

        template_values = {
            'navigation': structure.top_panel,
            }

        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render(template_values))


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)

for item in structure.top_panel:
    app.router.add((item['link'], item['handler']))

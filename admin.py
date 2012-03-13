import webapp2
import models
import jinja2
import os
import cgi
from datetime import datetime

class Event(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template(
            'templates/admin/create_event.html')
        self.response.out.write(template.render())

    def post(self):
        year = self.request.get('year')
        month = self.request.get('month')
        day = self.request.get('day')
        
        if month.isdigit() and year.isdigit() and day.isdigit():
            date = datetime(int(year), int(month), int(day))

            event = models.Event(tag=self.request.get('tag'),
                                 date=date,
                                 venue=self.request.get('venue'))
            event.put()                                   
            self.redirect('/admin/create_event')

class Talk(webapp2.RequestHandler):
    def get(self):
        #MAGIC
        events = models.Event.all().fetch(50)
        template_parameters = {'events': events}
        template = jinja_environment.get_template(
            'templates/admin/upload_talk.html')

        self.response.out.write(template.render(template_parameters))

    def post(self):
        talk = models.Talk(first_name=self.request.get('first_name'),
                           last_name=self.request.get('last_name'),
                           event_tag=self.request.get('event'),
                           topic=self.request.get('topic'),
                           foil=str(self.request.get('file')))

        talk.put()
        self.redirect('/admin/upload_talk')

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


app = webapp2.WSGIApplication([('/admin/upload_talk', Talk) ,
                              ('/admin/create_event', Event)],
                              debug=True)

import webapp2
import structure
import os
import jinja2
import models
from datetime import datetime

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class About(webapp2.RequestHandler):
    def get(self):
        pass

class Conference(webapp2.RequestHandler):
    def get(self):
        
        past_conferences = [
            {'date': 'today',
            },
            {'date': 'tomorrow',
             'presenters': [
                    {'name': 'John Doe',
                    'topic': 'breaking bad',
                    'foil_link': 'http://google.com',}
                    ],
             }
            ]
        
        upcoming_conferences = []
        #MAGIC
        events = models.Event.all().order('date').fetch(50)
        current_date = datetime.today()
        upcoming_events = []
        past_events = []

        #Use Query
        for event in events:
            talks = models.Talk.all().filter('event_tag =', event.tag)
            if talks.count():
                group = {'event': event.tag,
                         'talks': talks}
            else:
                group = {'event': event.tag}

            if event.date > current_date:
                upcoming_events.append(group)
            else:
                past_events.append(group)
                
        template_values = {
            'upcoming_events': upcoming_events,
            'past_events': past_events,
            'navigation': structure.top_panel,
            }
        template = jinja_environment.get_template('templates/conference.html')
        self.response.out.write(template.render(template_values))        

        
class Contact(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'navigation': structure.top_panel,
            'contacts': structure.contact_links,
            }

        template = jinja_environment.get_template('templates/contacts.html')
        self.response.out.write(template.render(template_values))        

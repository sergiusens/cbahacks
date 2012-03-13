from google.appengine.ext import db


class Navigation(db.Model):
    """Top pane"""
    name = db.StringProperty()
    link = db.StringProperty()
    order = db.IntegerProperty()
    show = db.BooleanProperty(False)

class Talk(db.Model):
    """Presenter that gave a talk sometime."""
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    topic = db.StringProperty()
    event_tag = db.StringProperty()
    foil = db.BlobProperty()

class Event(db.Model):
    """Manages events."""
    tag = db.StringProperty()
    date = db.DateTimeProperty()
    venue = db.StringProperty()
    
    

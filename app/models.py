from . import db  
import psycopg2
from datetime import datetime
from random import getrandbits 

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(80))
    bio = db.Column(db.String(400))
    image = db.Column(db.String(400))
    created_on = db.Column(db.DateTime)

   
    def generate_unique_id(self):
        return '15000%d' % getrandbits(16)

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __init__(self, firstname, lastname,username, age, gender, bio, image,created_on): 
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.age = age
        self.gender = gender
        self.bio = bio
        self.image = image
        self.created_on = datetime.now()
        #self.id = generate_unique_id(self)
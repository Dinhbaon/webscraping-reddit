from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, Text
from ast import literal_eval
import os
import pandas as pd

    

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'applicant.db')

df = pd.read_csv('..\csvfiles\processeddata.csv')

app.config['SQLALCHEMY_TRACK _MODIFICATIONS']=False
db = SQLAlchemy(app)


class attributes(db.Model): 
    __tablename__ = 'attributes'
    id = Column(Integer, primary_key=True)
    Gender = Column(String(10))
    SAT =Column(Integer)
    ACT = Column(Integer)
    Major =db.relationship('Major',backref = 'attributes') 
    ecs = db.relationship('Ecs', backref = 'attributes')
    Race = db.relationship('Race',backref = 'attributes')
    Acceptances = db.relationship('Acceptances', backref = 'attributes')
    Rejections = db.relationship('Rejections', backref = 'attributes')
    def __repr__(self):
        return f'<Attributes "{self.title}">'

class Ecs(db.Model):
    id = Column(Integer, primary_key = True)
    listofecs = Column(Text)
    Attributeid = Column(Integer, db.ForeignKey('attributes.id'))
    def __repr__(self):
        return f'<Ecs "{self.title}">'

class Major(db.Model): 
    id = Column(Integer, primary_key = True)
    majorlist = Column(Text)
    Attributeid = Column(Integer, db.ForeignKey('attributes.id'))
    def __repr__(self):
        return f'<major "{self.title}">'
class Race(db.Model):
    id = Column(Integer, primary_key = True)
    racelist = Column(Text)
    Attributeid = Column(Integer, db.ForeignKey('attributes.id'))
    def __repr__(self):
        return f'<race "{self.title}">'
class Acceptances(db.Model):
    id = Column(Integer, primary_key = True)
    acceptlist = Column(Text)
    Attributeid = Column(Integer, db.ForeignKey('attributes.id'))
    def __repr__(self):
        return f'<acceptances "{self.title}">'
class Rejections(db.Model):
    id = Column(Integer, primary_key = True)
    rejectlist = Column(Text)
    Attributeid = Column(Integer, db.ForeignKey('attributes.id'))
    def __repr__(self):
        return f'<rejections "{self.title}">'

@app.route('/')
def home(): 
    return 'Hello flask'

@app.route('/about') 
def about(): 
    return "This is the about page"
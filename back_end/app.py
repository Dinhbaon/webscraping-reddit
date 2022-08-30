from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer,VARCHAR, String, MetaData, Text
from ast import literal_eval
import os
import pandas as pd
from collections import Counter

    

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'applicant.db')
app.config['SQLALCHEMY_TRACK _MODIFICATIONS']=False
cors = CORS(app)
db = SQLAlchemy(app)
app.run(debug=True)

class attributes(db.Model): 
    __tablename__ = 'attributes'
    id = Column(Integer, primary_key=True)
    URL = Column(Text)
    Gender = Column(String(10))
    SAT =Column(Integer)
    ACT = Column(Integer)
    major =db.relationship('Major',backref = 'attributes') 
    ecs = db.relationship('Ecs', backref = 'attributes')
    Race = db.relationship('Race',backref = 'attributes')
    Acceptances = db.relationship('Acceptances', backref = 'attributes')
    Rejections = db.relationship('Rejections', backref = 'attributes')
    def get_data(): 
        ec = db.session.query(attributes).filter(Ecs.Attributeid == attributes.id).all()
        major = db.session.query(attributes).filter(Major.Attributeid == attributes.id).all()
        races = db.session.query(attributes).filter(Race.Attributeid==attributes.id).all()
        accepts = db.session.query(attributes).filter(Acceptances.Attributeid == attributes.id).all()
        rejects = db.session.query(attributes).filter(Rejections.Attributeid == attributes.id).all()
        data = db.session.query(attributes).all()
        majors = {}
        extracurriculars = {}
        race = {}
        acceptances = {}
        rejections = {}
        sat = {}
        act = {}
        gender = {}
        links = {}
        for row in data: 
            sat[row.id] = row.SAT
            act[row.id] = row.ACT
            gender[row.id] = row.Gender
            links[row.id] = row.URL
        for row in major: 
            majors[row.id] = []
            for maj in row.major:
                majors[maj.Attributeid].append(maj.majorlist)
        for row in ec:
            extracurriculars[row.id]  = []
            for extrac in row.ecs: 
                extracurriculars[extrac.Attributeid].append(extrac.listofecs)
        for row in races: 
            race[row.id] = []
            for r in row.Race: 
                race[r.Attributeid].append(r.racelist)
        for row in accepts: 
            acceptances[row.id] =[]
            for accept in row.Acceptances: 
                acceptances[accept.Attributeid].append(accept.acceptlist)
        for row in rejects: 
            rejections[row.id] = []
            for reject in row.Rejections: 
                rejections[reject.Attributeid].append(reject.rejectlist)
        dataset ={'Gender':gender, 'SAT':sat, 'ACT':act,'Majors': majors,'Ecs':extracurriculars,'Race':race, 'Acceptances':acceptances, 'Rejections':rejections, "URL": links}
        return dataset

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

@app.route('/api/<string:column>/value', methods = ['GET'])
def home(column : str): 
    return list(attributes.get_data()[column].values())

@app.route('/api/<string:column>', methods = ['GET'])
def dict(column : str): 
    return attributes.get_data()[column]


@app.route('/api/<string:column>/value/count',methods = ['GET'])
def count(column:str): 
    return Counter(attributes.get_data()[column].values())

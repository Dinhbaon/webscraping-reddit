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
    def get_gender(): 

        # races = db.session.query(attributes).filter(Race.Attributeid==attributes.id).all()

        data = db.session.query(attributes.Gender, attributes.id).all()
        # extracurriculars = {}
        # race = {}

        gender = {}
        for row in data: 
            gender[row.id] = row.Gender
        # for row in races: 
        #     race[row.id] = []
        #     for r in row.Race: 
        #         race[r.Attributeid].append(r.racelist)


        return gender
    def get_SAT(): 
        sat = {}
        datasat = db.session.query(attributes.SAT,attributes.id).all()
        for row in datasat: 
            sat[row.id] = row.SAT
        return sat
    def get_ACT(): 
        dataact = db.session.query(attributes.ACT,attributes.id).all()
        act={}
        for row in dataact: 
            act[row.id] = row.ACT
        return act
    def get_links(): 
        links = {}
        datalinks = db.session.query(attributes.URL,attributes.id).all()
        for row in datalinks: 
            links[row.id] = row.URL
        return links
    def get_major():
        major = db.session.query(attributes).filter(Major.Attributeid == attributes.id).all()
        majors = {} 
        for row in major: 
            majors[row.id] = []
            for maj in row.major:
                majors[maj.Attributeid].append(maj.majorlist)
        return majors
    def get_accept(): 
        accepts = db.session.query(attributes).filter(Acceptances.Attributeid == attributes.id).all()
        acceptances = {}
        for row in accepts: 
            acceptances[row.id] =[]
            for accept in row.Acceptances: 
                acceptances[accept.Attributeid].append(accept.acceptlist)
        return acceptances
    def get_reject(): 
        rejects = db.session.query(attributes).filter(Rejections.Attributeid == attributes.id).all()
        rejections = {}
        for row in rejects: 
            rejections[row.id] = []
            for reject in row.Rejections: 
                rejections[reject.Attributeid].append(reject.rejectlist)
        return rejections
    def get_ecs(): 
        ec = db.session.query(attributes).filter(Ecs.Attributeid == attributes.id).all()
        extracurriculars = {}
        for row in ec:
            extracurriculars[row.id]  = []
            for extrac in row.ecs: 
                extracurriculars[extrac.Attributeid].append(extrac.listofecs)
        return extracurriculars

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

# @app.route('/api/<string:column>/value', methods = ['GET'])
# def home(column : str): 
#     return list(attributes.get_data()[column].values())

@app.route('/api/Gender', methods = ['GET'])
def gender(): 
    return attributes.get_gender()
@app.route('/api/URL', methods = ['GET'])
def url(): 
    return attributes.get_links()
@app.route('/api/SAT', methods = ['GET'])
def sat(): 
    return attributes.get_SAT()
@app.route('/api/ACT',methods = ['GET'])
def act(): 
    return attributes.get_ACT
@app.route('/api/Majors', methods = ['GET'])
def major(): 
    return attributes.get_major()
@app.route('/api/Acceptances', methods = ['GET'])
def accept(): 
    return attributes.get_accept()
@app.route('/api/Rejections', methods = ['GET'])
def reject(): 
    return attributes.get_reject()
@app.route('/api/Extracurriculars', method = ['GET'])
def ecs(): 
    return attributes.get_ecs()


# @app.route('/api/<string:column>/value/count',methods = ['GET'])
# def count(column:str): 
#     return Counter(attributes.get_data()[column].values())

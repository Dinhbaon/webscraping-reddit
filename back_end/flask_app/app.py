import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String,Text, func, desc, asc
import os
from flask_marshmallow import Marshmallow
from flask_caching import Cache
config={'CACHE_TYPE': 'SimpleCache'}




app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
#mysql+pymysql://root:Kimthanh142@127.0.0.1:{}/applicants'.format
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK _MODIFICATIONS']=False
cors = CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config.from_mapping(config)

cache = Cache(app)


class attributes(db.Model):
    __tablename__ = 'attributes'
    URL = Column(Text)
    Gender = Column(String(20))
    SAT =Column(String(10))
    ACT = Column(String(10))
    timestamp = Column(Integer, primary_key = True, index = True)
    major =db.relationship('Major',backref = 'attributes', lazy="joined")
    ecs = db.relationship('Ecs', backref = 'attributes', lazy="joined")
    Race = db.relationship('Race',backref = 'attributes', lazy="joined")
    Acceptances = db.relationship('Acceptances', backref = 'attributes', lazy="joined")
    Rejections = db.relationship('Rejections', backref = 'attributes', lazy="joined")
    def get_gender():

        data = db.session.query(attributes.Gender, attributes.timestamp).all()
        gender = {}
        for row in data:
            gender[row.timestamp] = row.Gender

        return gender
    def get_SAT():
        sat = {}
        datasat = db.session.query(attributes.SAT,attributes.timestamp).all()
        for row in datasat:
            sat[row.timestamp] = row.SAT
        return sat
    def get_ACT():
        dataact = db.session.query(attributes.ACT,attributes.timestamp).all()
        act={}
        for row in dataact:
            act[row.timestamp] = row.ACT
        return act
    def get_links():
        links = {}
        datalinks = db.session.query(attributes.URL,attributes.timestamp).order_by(attributes.timestamp.desc()).all()
        for row in datalinks:
            links[row.timestamp] = row.URL
        return links
    # def get_major():
    #     major = db.session.query(attributes).filter(Major.Attributeid == attributes.id).all()
    #     majors = {}
    #     for row in major:
    #         majors[row.id] = []
    #         for maj in row.major:
    #             majors[maj.Attributeid].append(maj.majorlist)
    #     return majors
    # def get_accept():
    #     accepts = db.session.query(attributes).filter(Acceptances.Attributeid == attributes.id).all()
    #     acceptances = {}
    #     for row in accepts:
    #         acceptances[row.id] =[]
    #         for accept in row.Acceptances:
    #             acceptances[accept.Attributeid].append(accept.acceptlist)
    #     return acceptances
    # def get_reject():
    #     rejects = db.session.query(attributes).filter(Rejections.Attributeid == attributes.id).all()
    #     rejections = {}
    #     for row in rejects:
    #         rejections[row.id] = []
    #         for reject in row.Rejections:
    #             rejections[reject.Attributeid].append(reject.rejectlist)
    #     return rejections
    # def get_ecs():
    #     ec = db.session.query(attributes).filter(Ecs.Attributeid == attributes.id).all()
    #     extracurriculars = {}
    #     for row in ec:
    #         extracurriculars[row.id]  = []
    #         for extrac in row.ecs:
    #             extracurriculars[extrac.Attributeid].append(extrac.listofecs)
    #     return extracurriculars

class Ecs(db.Model):
    id = Column(Integer, primary_key = True)
    listofecs = Column(String(20))
    Attributeid = Column(Integer, db.ForeignKey('attributes.timestamp'))
    def __repr__(self):
        return f'<Ecs "{self.title}">'
class Major(db.Model):

    id = Column(Integer, primary_key = True)
    majorlist = Column(String(20))
    Attributeid = Column(Integer, db.ForeignKey('attributes.timestamp'))

class Race(db.Model):
    id = Column(Integer, primary_key = True)
    racelist = Column(String(20))
    Attributeid = Column(Integer, db.ForeignKey('attributes.timestamp'))
    def __repr__(self):
        return f'<race "{self.title}">'
class Acceptances(db.Model):
    id = Column(Integer, primary_key = True)
    acceptlist = Column(String(50))
    Attributeid = Column(Integer, db.ForeignKey('attributes.timestamp'))
    def __repr__(self):
        return f'<acceptances "{self.title}">'
class Rejections(db.Model):
    id = Column(Integer, primary_key = True)
    rejectlist = Column(String(50))
    Attributeid = Column(Integer, db.ForeignKey('attributes.timestamp'))
    def __repr__(self):
        return f'<rejections "{self.title}">'

# @app.route('/api/<string:column>/value', methods = ['GET'])
# def home(column : str):
#     return list(attributes.get_data()[column].values())

@app.route('/api/Gender', methods = ['GET'])
def gender():
    return json.dumps(attributes.get_gender())

@app.route('/api/URL', methods = ['GET'])
def url():
    return json.dumps(attributes.get_links())

@app.route('/api/SAT', methods = ['GET'])
def sat():
    return attributes.get_SAT()

@app.route('/api/ACT',methods = ['GET'])
def act():
    return attributes.get_ACT()

@app.route('/api/Majors', methods = ['GET'])
@cache.cached(timeout=600)
def major():
    distinct_parent_ids = db.session.query(Major.Attributeid).distinct().subquery()

    # get the majorlist values and group by parent_id
    result = db.session.query(
    Major.Attributeid,
    func.group_concat(Major.majorlist).label("majorlist")
    ).filter(
    Major.Attributeid.in_(distinct_parent_ids)
    ).group_by(
    Major.Attributeid
    )

    # convert the result to a dictionary
    result_dict = {row.Attributeid: row.majorlist.split(',') if row.majorlist else [] for row in result}

    return(result_dict)
@app.route('/api/Acceptances', methods = ['GET'])
@cache.cached(timeout=600)
def accept():
    distinct_parent_ids = db.session.query(Acceptances.Attributeid).distinct().subquery()

    # get the majorlist values and group by parent_id
    result = db.session.query(
    Acceptances.Attributeid,
    func.group_concat(Acceptances.acceptlist).label("acceptlist")
    ).filter(
    Acceptances.Attributeid.in_(distinct_parent_ids)
    ).group_by(
    Acceptances.Attributeid
    )

    # convert the result to a dictionary
    result_dict = {row.Attributeid: row.acceptlist.split(',') if row.acceptlist else [] for row in result}

    return(result_dict)


@app.route('/api/Rejections', methods = ['GET'])
@cache.cached(timeout=600)
def reject():
    distinct_parent_ids = db.session.query(Rejections.Attributeid).distinct().subquery()
    # get the majorlist values and group by parent_id
    result = db.session.query(
    Rejections.Attributeid,
    func.group_concat(Rejections.rejectlist).label("rejectlist")
    ).filter(
    Rejections.Attributeid.in_(distinct_parent_ids)
    ).group_by(
    Rejections.Attributeid
    )

    # convert the result to a dictionary
    result_dict = {row.Attributeid: row.rejectlist.split(',') if row.rejectlist else [] for row in result}

    return(result_dict)

@app.route('/api/Extracurriculars', methods = ['GET'])
@cache.cached(timeout=600)
def ecs():
    distinct_parent_ids = db.session.query(Ecs.Attributeid).distinct().subquery()

    # get the majorlist values and group by parent_id
    result = db.session.query(
    Ecs.Attributeid,
    func.group_concat(Ecs.listofecs).label("listofecs")
    ).filter(
    Ecs.Attributeid.in_(distinct_parent_ids)
    ).group_by(
    Ecs.Attributeid
    )

    # convert the result to a dictionary
    result_dict = {row.Attributeid: row.listofecs.split(',') if row.listofecs else [] for row in result}

    return(result_dict)


# @app.route('/api/<string:column>/value/count',methods = ['GET'])
# def count(column:str):
#     return Counter(attributes.get_data()[column].values())

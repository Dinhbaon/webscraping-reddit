from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, MetaData
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK _MODIFICATIONS']=False
db = SQLAlchemy(app)

metadataobj = MetaData()

data = Table('applicants',metadataobj,db.Column())

@app.route('/')
def home(): 
    return 'Hello flask'

@app.route('/about') 
def about(): 
    return "This is the about page"
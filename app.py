from flask import Flask, render_template, request
#from .app_db import DB, Project
from os import getenv
from flask_sqlalchemy import SQLAlchemy

# app instantiation
#APP = flask_app()
APP = Flask(__name__)

# app_db
DB = SQLAlchemy()

# Connect our database to the app object
DB.init_app(APP)

class Project(DB.Model):
    """SQLA table for Project info"""
    # unique id for project obj
    id = DB.Column(DB.BigInteger, primary_key=True)
    # name column
    name = DB.Column(DB.String, nullable=False)
    # description of product/service
    description = DB.Column(DB.String(1000), nullable=True)
    # amount the kickstarter aims to reach
    goal = DB.Column(DB.BigInteger, nullable=False)
    # sub category of product/service
    category = DB.Column(DB.String, nullable=False)
    # how long to reach goal (campaign length)
    duration = DB.Column(DB.BigInteger, nullable=False)
    

    def __repr__(self):
        return "<Project: {}>".format(self.name)


# configuring to database
APP.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# this is a functino to create app
def flask_app():
    '''This app creates our application'''

    # creating db model around app
    DB.init_app(APP)

    # -----HOME ROUTE------
    @APP.route('/')
    def Home_page():
        '''Landing page to the Kickstarter Prediction project'''

        return render_template('landing.html', title='Home')

    def df_creator():
        '''creates table from inputted user data'''
    
    # -----RESET DB------
    @APP.route('/reset')
    def reset():
        # empty db
        DB.drop_all()
        # recreate tables
        DB.create_all()

        return render_template('landing.html', title='database has been reset')
    
    return APP

APP = flask_app()

def data_retrieval():
    # database objects
    projects = Project.query.all()
    # list of individual kickstarters
    kickstarters = []
    # iterating over every project
    for project in projects:
        # filling empty list
        kickstarters.append(project.name)
        # return full list
    return kickstarters

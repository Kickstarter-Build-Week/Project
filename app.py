from flask import Flask, render_template, request
from .app_db import DB, Project
from os import getenv

# app instantiation
APP = Flask(__name__)
# configuring to database
APP.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect our database to the app object
DB.init_app(APP)

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

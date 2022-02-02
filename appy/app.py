from flask import Flask, render_template, request
from .app_db import DB
from .predict import *


# app instantiation
APP = Flask(__name__)
# configuring to database
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# this is a functino to create app
def flask_app():
    '''This app creates our application'''
    
    # creating db model around app
    DB.init_app(APP)

    # home route
    @APP.route('/')
    def Home_page():
        '''Landing page to the Kickstarter Prediction project'''
    
        return render_template('landing.html', title='Home')

    def df_creator():
        '''creates table from inputted user data'''
    
    # for resetting db of inputted user data
    @APP.route('/reset')
    def reset():
        # empty db
        DB.drop_all()
        # recreate tables
        DB.create_all()

        return render_template('landing.html', title='database has been reset')
    
    return APP
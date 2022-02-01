from flask import Flask, render_template, request
from .app_db import DB, Project

# this is a functino to create app
def flask_app():
    '''This app creates our application'''

    # app instantiation
    APP = Flask(__name__)

    # configuring to database
    APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # creating db model around app
    DB.init_app(APP)

    # home route
    @APP.route('/')
    def Home_page():
        '''Landing page to the Kickstarter Prediction project'''
        
        return render_template('landing.html', title='Home')
    def df_creator():
        '''creates table from inputted user data'''
        
    return APP
from flask import Flask, render_template, request
from app_dependencies.userdata import DB, Project
# app instantiation
APP = Flask(__name__)

# configuring to database
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connecting app to database

# this is a functino to create app
def flask_app():
    '''This app creates our application'''
    @APP.route('/')
    def Home_page():
        '''Landing page to the Kickstarter Prediction project'''
        
        return render_template('landing.html', title='Home')

    return APP
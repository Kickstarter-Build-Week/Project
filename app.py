from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


APP = FLASK(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(APP)
DB.init_app(APP)

# this is a functino to create app
def create_app():
    '''This app creates our application'''
    @APP.route('/')
    def root():
        '''Landing page to the Kickstarter Prediction project'''
        
        return render_template('landing.html', title='Home')

    return APP
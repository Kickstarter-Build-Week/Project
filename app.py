from hashlib import new
from flask import Flask, render_template, request
from os import getenv
import pickle
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from flask_sqlalchemy import SQLAlchemy

# database instantiation
DB = SQLAlchemy()

# app instantiation
APP = Flask(__name__)

# Load model
with open("xgb_class_1.pkl", "rb") as f:
    model = pickle.load(f)
    #X = df[['name_len', 'blurb_len', 'goal', 'launch_to_deadline_days', 'category']]
    #y = model.XGboost(df) # Return a 0(predicts fail) or 1(predicts successful)


# Connect our database to the app object
DB.init_app(APP)

# configuring to database
APP.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask_sqlalchemy import SQLAlchemy





# _______PROJECT OBJECT_________
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

# goal', 'name_len', 'blurb_len', 'category_academic', 'category_apps',
#        'category_blues', 'category_comedy', 'category_experimental',
#        'category_festivals', 'category_flight', 'category_gadgets',
#        'category_hardware', 'category_immersive', 'category_makerspaces',
#        'category_musical', 'category_places', 'category_plays',
#        'category_restaurants', 'category_robots', 'category_shorts',
#        'category_software', 'category_sound', 'category_spaces',
#        'category_thrillers', 'category_wearables', 'category_web',
#        'category_webseries', 'campaign_length_days'


def create_project_df(name, blurb, goal, category, length):
    # function to process user input and make a dataframe
    ks = pd.DataFrame(columns = ['name', 'blurb', 'goal','category', 'length'])
    nlen = len(name.split())
    blen = len(blurb.split())
    ks.loc[len(ks.index)] = [nlen, blen, goal, category, length]


# this is a function to create app
def flask_app():
    '''This app creates our application'''


    # -----HOME ROUTE------
    @APP.route('/')
    def Home_page():
        '''Landing page to the Kickstarter Prediction project'''
        return render_template('landing.html', title='Home')

    # -----RESET DB------
    @APP.route('/reset')
    def reset():
        # empty db
        DB.drop_all()
        # recreate tables
        DB.create_all()

        return render_template('landing.html', title='database has been reset')

    @APP.route('/project', methods= ['GET', 'POST'])
    def update_project():
        if request.method == 'POST':
            prj_name = request.form['prj']
            prj_desc = request.form['blurb']
            prj_goal = request.form['goal']
            prj_category = request.form['category']
            prj_length = request.form['length']
            db_project = Project(name=prj_name,
                                 description=prj_desc,
                                 goal=prj_goal,
                                 category=prj_category,
                                 duration=prj_length)
            ks = create_project_df(prj_name, prj_desc, prj_goal, prj_category, prj_length)
            DB.session.add(db_project)
            DB.session.commit()
        else:
            render_template('forms.html')
            
        


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

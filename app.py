from flask import Flask, render_template, request, redirect, url_for
from os import getenv
from flask_sqlalchemy import SQLAlchemy
import pickle
import pandas as pd

# app instantiation
APP = Flask(__name__)

# Load model
with open("xgb_class_1.pkl", "rb") as f:
    model = pickle.load(f)
    # X = df[['name_len', 'blurb_len', 'goal', 'launch_to_deadline_days', 'category']]
    #y = model.XGboost(df) # Return a 0(predicts fail) or 1(predicts successful)

# app_db
DB = SQLAlchemy()

# Connect our database to the app object
DB.init_app(APP)

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

# configuring to database
APP.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def create_project_df(name, blurb, goal, category, length):
    # function to process user input and make a dataframe

    # list all columns needed for model
    cols = ['goal', 'name_len', 'blurb_len', 'category_academic',
            'category_apps', 'category_blues', 'category_comedy', 
            'category_experimental', 'category_festivals', 'category_flight', 
            'category_gadgets', 'category_hardware', 'category_immersive', 
            'category_makerspaces', 'category_musical', 'category_places', 
            'category_plays', 'category_restaurants', 'category_robots', 
            'category_shorts', 'category_software', 'category_sound', 
            'category_spaces','category_thrillers', 'category_wearables', 
            'category_web','category_webseries', 'campaign_length_days']

    nlen = len(name.split())
    blen = len(blurb.split())
    cat = "category_" + category.lower()

    # Create a dataframe with 1 row with only 0's
    ks = pd.DataFrame(columns = cols)
    ks.loc[len(ks.index)] = 0

    # Add our variables to the dataframe
    ks['goal'] = goal
    ks['name_len'] = nlen
    ks['blurb_len'] = blen
    ks['campaign_length_days'] = length

    # "OneHotEncode" our category
    for col in ks.columns:
        if cat == col:
            ks[col] = 1

    return ks

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

@APP.route('/prediction', methods= ["POST"])
def prediction():
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
    predify = model.predict(ks)
    if predify == [0]:
        pred_result = 'a failure.'
    if predify == [1]:
        pred_result = 'a successful bastard.' 
    # DB.session.add(db_project)
    # DB.session.commit()
    return render_template('prediction.html',
                           title="Prediction",
                           prediction=pred_result)
                        #    project=prj_name,
                        #    prj_desc=prj_desc,
                        #    prj_goal=prj_goal,
                        #    prj_category=prj_category,
                        #    prj_length=prj_length)
    #return render_template('prediction.html', title='Prediction')

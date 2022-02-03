from hashlib import new
from flask import Flask, render_template, request
from os import getenv
from .app_db import DB, Project
import pickle


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

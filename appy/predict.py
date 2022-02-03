import pandas as pd
import pickle
from .app import DB, Project


# xgb_model_loaded = pickle.load(open('xgb_class_1.pkl', "rb"))
# 'name', → needs to be turned into ‘name_len’ { get number of words: len(name.split()) }
# 'blurb', → needs to be turned into ‘blurb_len’ { get number of words: len(blurb.split()) }
# 'goal',
# 'category', → OneHotEncode (use pd.get_dummies, I will share code during meeting)
# ‘campaign_length_days’

def create_project_df(name, blurb, goal, category, length):
    ks = pd.DataFrame(columns = ['name', 'blurb', 'goal','category', 'length'])
    ks.loc[len(ks.index)] = [name, blurb, goal, category, length]


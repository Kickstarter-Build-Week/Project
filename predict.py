import pandas as pd
import pickle


# xgb_model_loaded = pickle.load(open('xgb_class_1.pkl', "rb"))
# 'name', → needs to be turned into ‘name_len’ { get number of words: len(name.split()) }
# 'blurb', → needs to be turned into ‘blurb_len’ { get number of words: len(blurb.split()) }
# 'goal',
# 'category', → OneHotEncode (use pd.get_dummies, I will share code during meeting)
# ‘campaign_length_days’

category = ['Academic', 'Places', 'Blues', 'Restaurants', 'Webseries',
       'Thrillers', 'Shorts', 'Web', 'Apps', 'Gadgets', 'Hardware',
       'Festivals', 'Plays', 'Musical', 'Flight', 'Spaces', 'Immersive',
       'Experimental', 'Comedy', 'Wearables', 'Sound', 'Software',
       'Robots', 'Makerspaces']

def create_project(name, blurb, goal, category, length):
    ks = pd.DataFrame(columns = ['name', 'blurb', 'goal','category', 'length'])
    ks.loc[len(ks.index)] = [name, blurb, goal, category, length]
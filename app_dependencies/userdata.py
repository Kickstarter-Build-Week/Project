from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class Project(DB.Model):
    """SQLA table for Project info"""
    # unique id for project obj
    id = DB.Column(DB.BigInteger, primary_key=True)
    # name column
    name = DB.Column(DB.String, nullable=False)
    # amount the kickstarter aims to reach
    goal = DB.Column(DB.BigInteger, nullable=False)
    # sub category of product/service
    category = DB.Column(DB.String, nullable=False)
    # main category of product/service
    Topic = DB.Column(DB.String, nullable=False)
    # how long to reach goal (campaign length)
    duration = DB.Column(DB.BigInteger, nullable=False)
    # description of product/service
    description = DB.Column(DB.String(1000), nullable=True)
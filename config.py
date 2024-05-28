import os

DB_NAME = "database.db"
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'd329419510d8a8f0d6135315dfce2cfea69e434ac42fd3868fa58ce826cb0247'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, f'{DB_NAME}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
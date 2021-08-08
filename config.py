import os

class Config:
    FLASK_ENV = 'development'
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')

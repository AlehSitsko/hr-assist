import os

basedir = os.path.abspath(os.path.dirname(__file__))    


# Configuration file for the Flask application

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' #Change this to a strong secret key
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'another-secret-key' # Change this to a strong JWT secret key
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    ADMIN_USERNAME = 'Welcome' # Change this to your desired admin username
    ADMIN_PASSWORD = 'Utop1631' # Change this to your desired admin password
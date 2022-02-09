import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOSSIER_PER_PAGE = 4
    UPLOAD_FOLDER = os.path.join(basedir, 'app/templates/static')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'jpeg', 'jpg'}
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

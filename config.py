import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1/project'
    DOSSIER_PER_PAGE = 4
    UPLOAD_FOLDER = os.path.join(basedir, 'app/templates/static')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'jpeg', 'jpg'}
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    # Flask-Security config
    SECURITY_URL_PREFIX = "/auth"
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

    # Flask-Security URLs, overridden because they don't put a / at the end
    # SECURITY_LOGIN_URL = "/login"
    # SECURITY_LOGOUT_URL = "/logout/"
    # SECURITY_REGISTER_URL = "/register/"

    # Flask-Security features
    SECRET_REGISTERABLE = True
    SECRET_SEND_REGISTER_EMAIL = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


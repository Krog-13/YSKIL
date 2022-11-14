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
    UPLOAD_FOLDER = os.path.join(basedir, 'app/static/docs')
    ALLOWED_EXTENSIONS = {'docx', 'pdf', 'jpeg'}
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    # Flask-Security config
    SECURITY_URL_PREFIX = "/auth"
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['virtualspook@gmail.com'] #swwunyunvaejdyjg
    # Flask-Security URLs, overridden because they don't put a / at the end
    # SECURITY_LOGIN_URL = "/login"
    # SECURITY_LOGOUT_URL = "/logout/"
    # SECURITY_REGISTER_URL = "/register/"

    # Flask-Security features
    SECRET_REGISTERABLE = True
    SECRET_SEND_REGISTER_EMAIL = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


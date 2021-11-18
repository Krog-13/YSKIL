from app import app, db
from flask import request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app.forms import UploadForm, PostForm




def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    return render_template('index.html')



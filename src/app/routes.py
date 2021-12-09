from app import app, db
from flask import request, redirect, url_for, flash, render_template, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app.forms import UploadForm, PostForm, LoginForm, RegisterForm
from app.models import Achievements, User
import os


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    page = request.args.get('page', 1, type=int)
    dossier = Achievements.query.order_by(Achievements.timestamp.desc()).paginate(
        page, app.config['DOSSIER_PER_PAGE'], False)
    next_url = url_for('index', page=dossier.next_num) \
        if dossier.has_next else None
    prev_url = url_for('index', page=dossier.prev_num) \
        if dossier.has_prev else None
    return render_template('index.html', title='Home', posts=dossier.items, next_url=next_url, prev_url=prev_url)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.passwrod.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sing in', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.achieves.order_by(Achievements.timestamp.desc())
    return render_template('user.html', user=user, posts=posts)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = PostForm()
    filename = None
    if form.validate_on_submit():
        f = form.doc.data
        if f:
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        post = Achievements(subject=form.subject.data,
                            body=form.body.data,
                            author=current_user,
                            certificate=filename)
        db.session.add(post)
        db.session.commit()
        flash('Your skill has been added')

        return redirect(url_for('index'))
    return render_template('edit_profile.html', form=form)

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

def testsqlite():
    pass

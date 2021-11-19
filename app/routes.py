from app import app, db
from flask import request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app.forms import UploadForm, PostForm
from app.models import Achievements, User



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

@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.achieves.order_by(Achievements.timestamp.desc())
    return render_template('user.html', user=user, posts=posts)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = PostForm()
    if form.validate_on_submit():
        post = Achievements(subject=form.subject.data,
                            body=form.body.data,
                            author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your skill has been added')
    return render_template('edit_profile.html', form=form)
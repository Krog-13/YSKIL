from app import db
from app.main import bp
from flask import request, redirect, url_for, flash, render_template, send_from_directory, current_app
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app.main.forms import PostForm, TalentForm
from app.models import Achievements, User, Branches
import os


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    page = request.args.get('page', 1, type=int)
    dossier = Achievements.query.order_by(Achievements.timestamp.desc()).paginate(
        page, current_app.config['DOSSIER_PER_PAGE'], False)
    next_url = url_for('main.index', page=dossier.next_num) \
        if dossier.has_next else None
    prev_url = url_for('main.index', page=dossier.prev_num) \
        if dossier.has_prev else None
    return render_template('index.html', title='Home', posts=dossier.items, next_url=next_url, prev_url=prev_url)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.achieves.order_by(Achievements.timestamp.desc())
    return render_template('user.html', user=user, posts=posts)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = PostForm()
    filename = None
    if form.validate_on_submit():
        f = form.summary.data
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        post = Achievements(subject=form.subject.data,
                            body=form.body.data,
                            author=current_user,
                            summary=filename)
        db.session.add(post)
        db.session.commit()
        flash('Your skill has been added')

        return redirect(url_for('main.index'))
    return render_template('edit_profile.html', form=form)


@bp.route('/branch/<username>', methods=['GET', 'POST'])
@login_required
def branch(username):
    form = TalentForm()
    filename, is_type_exists = None, []
    user = User.query.filter_by(username=username).first_or_404()
    certificates = user.branches.order_by(Branches.timestamp.desc())
    for i in certificates:
        is_type_exists.append(i.field)
    if form.validate_on_submit():
        f = form.doc.data
        # is_type_exists = Branches.query.filter_by(user_id=user.id, field=form.field.data)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            post = Branches(certificate=filename,
                            field=form.field.data,
                            title=form.title.data,
                            timestamp=form.datetime.data,
                            organization=form.organisation.data,
                            author=current_user)
            db.session.add(post)
            db.session.commit()
            flash('Your skill has been added')
            return redirect(url_for('main.branch', username=username))
        flash(f'Invalid extension - {f.filename}')
    return render_template('branch.html', form=form, posts=certificates, type=is_type_exists)


@bp.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], name)
from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(400))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    achieves = db.relationship('Achievements', backref='author', lazy='dynamic')
    branches = db.relationship('Branches', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<- User {self.username} ->'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?s={}'.format(digest, size)


class Achievements(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(120), unique=True)
    body = db.Column(db.String(140))
    certificate = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<- Achieve {self.subject} ->'


class Branches(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    certificate = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    level = db.Column(db.String(80), default='Easy')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<- Branches {self.level} ->'
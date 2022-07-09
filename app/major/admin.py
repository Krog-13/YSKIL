from app import admin, db
from app.models import User, Achievements, Branches
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, request
from flask_login import current_user


class SkillView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))

admin.add_view(SkillView(User, db.session))
admin.add_view(SkillView(Branches, db.session))
admin.add_view(SkillView(Achievements, db.session))
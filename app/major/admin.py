from app import admin, db
from app.models import User, Achievements, Branches, Role
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, request
# from flask_login import current_user
from flask_admin import helpers as admin_helpers
from flask_security import Security, SQLAlchemyUserDatastore, current_user


class UsersView(ModelView):

    page_size = 25
    can_edit = False
    column_export_list = ["password_hash"]
    column_searchable_list = ["email"]
    create_modal = True
    edit_modal = True
    column_labels = {
        "username":'User',
        "last_seen": "Date"
    }
    column_exclude_list = ["password_hash", "token"]


    def is_accessible(self):
        return (current_user.is_authenticated and
                current_user.has_role('superuser'))

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))

class SkillView(ModelView):

    def is_accessible(self):
        return (current_user.is_authenticated and
                current_user.has_role('superuser'))

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))



def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
    )


def security(app):
    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    Security(app, user_datastore)
    security_context_processor()


admin.add_view(UsersView(User, db.session))
admin.add_view(SkillView(Branches, db.session))
admin.add_view(SkillView(Achievements, db.session))



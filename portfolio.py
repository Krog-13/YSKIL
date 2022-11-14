from app import create_app, db
from app.models import User, Achievements, Role


app = create_app()
from app.major import admin

admin.security(app)


@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Achievements, 'Role': Role}

if __name__ == '__main__':
    app.run()
from app import create_app, db
from app.models import User, Achievements

app = create_app()
from app.major import admin

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Achievements}


if __name__ == '__main__':
     app.run()
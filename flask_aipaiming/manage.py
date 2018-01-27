from flask_script import Manager

from app.models import Apm_Users
from app import app

manager = Manager(app)


@manager.command
def save():
    todo = Apm_Users(user_login="study flask")
    todo.save()


@manager.command
def query_all():
    # users = User.query_all()
    users = Apm_Users.query.all()
    for u in users:
        print  u


if __name__ == '__main__':
    manager.run()

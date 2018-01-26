from flask_script import Manager

from app import Todo
from app import app

manager = Manager(app)


@manager.command
def save():
    todo = Todo(content="study flask")
    todo.save()


if __name__ == '__main__':
    manager.run()
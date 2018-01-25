#encoding=utf-8
from flask_script import Manager
from app import  app
from models import  User

manager = Manager(app)

@manager.command
def save():
     # user = User('zhangjie','zhangjie@zhangjie.com')
     # user.save()
     user = User(name='zhangjie02',email='zhangjie02@126.com')
     user.save()

@manager.command
def query_users():
    #users = User.query_users()
    users = User.objects.find()
    for user in users:
        print  user

if __name__ == '__main__':
    manager.run()
from flask_script import Manager
from app import  app
import  sqlite3
from models import User
manager = Manager(app)

@manager.command
def hello():
    print 'Hello World!'

@manager.option('-m','--msg',dest='msg_val',default='world')
def hello_world(msg_val):
    print 'hello'+msg_val

@manager.command
def init_db():
    sql ='create table user (id INT ,name TEXT)'
    con =sqlite3.connect("test.db")
    cursor =con.cursor()
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()

@manager.command
def save():
    user = User(1,'zhangjie')
    user.save()

@manager.command
def query_all():
    users = User.query()
    for user in users:
        print user



if __name__ == '__main__':
    manager.run()

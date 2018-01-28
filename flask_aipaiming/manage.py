# -*- coding: UTF-8 -*-
from flask_script import Manager
from datetime import datetime
from app.models import ApmUsers,Apmuser,ApmTerms
from app import app

from app import db

manager = Manager(app)


@manager.command
def save_login():
    apm_users = ApmUsers(100, 'zhangjie','123456','zj','zj@126.com','123','123','1','1','2018-01-28 11:11:11')
    db.session.add(apm_users)
    db.session.commit()


@manager.command
def query_all_login():
    apm_users = ApmUsers.query.all()
    for u in apm_users:
        print  u


@manager.command
def save_user():
     apm_user = Apmuser(3,'zhangjie33','444')
     db.session.add(apm_user)
     db.session.commit()


@manager.command
def query_all_user():
    users =Apmuser.query.all()
    for u in users:
        print  u


@manager.command
def save_item():
     apmterms = ApmTerms(None,'test','444',0)
     db.session.add(apmterms)
     db.session.commit()



@manager.command
def query_all_item():
    apmterms =ApmTerms.query.all()
    for u in apmterms:
        print  u


if __name__ == '__main__':
    manager.run()

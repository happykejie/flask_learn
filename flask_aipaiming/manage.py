# -*- coding: UTF-8 -*-
from flask_script import Manager
from datetime import datetime
from app.models import ApmUsers,ApmTerms, ApmPosts
from app import app
from flask import jsonify

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
        print u.user_login

@manager.command
def add_post():
    currenttime = '2018-01-30 10:10:11'#datetime.year +'-'+datetime.month+'-'+datetime.day+' '+datetime.hour+':'+datetime.minute+':'+datetime.second
    apm_post = ApmPosts(None, 1,currenttime,currenttime,'这是一个测试','测试'
                        ,'测试1','1','1','1','password','post_name','123','123',currenttime
                        ,currenttime,'123',1,'123',2,'123','123',1000)
    db.session.add(apm_post)
    db.session.commit()


@manager.command
def query_posts():
    apm_posts = ApmPosts.query.filter_by(post_title='测试').first()
    #for u in apm_posts:
    return  apm_posts.post_title








if __name__ == '__main__':
    manager.run()

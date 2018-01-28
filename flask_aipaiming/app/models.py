# -*- coding: UTF-8 -*-
import  MySQLdb
from app import  db
from datetime import datetime


class ApmUsers(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    user_login =db.Column(db.String(60))
    user_pass =db.Column(db.String(255))
    user_nicename =db.Column(db.String(50))
    user_email =db.Column(db.String(100))
    user_url =db.Column(db.String(1000))
    user_registered =db.Column(db.DateTime)
    user_activation_key =db.Column(db.String(255))
    user_status =db.Column(db.INTEGER)
    display_name =db.Column(db.VARCHAR(250))

    def __init__(self, ID,user_login, user_pass, user_nicename, user_email,user_url
                 ,user_activation_key,user_status,display_name,user_registered):
        self.ID =ID
        self.user_login = user_login
        self.user_pass = user_pass
        self.user_nicename = user_nicename
        self.user_email = user_email
        self.user_url = user_url
        self.user_activation_key = user_activation_key
        self.user_status =user_status
        self.display_name = display_name
        self.user_registered = user_registered

    def __repr__(self):
        return '<Apm_Users %r>' % self.user_login


# 定义数据模型类
# class User(db.Model):
#     # 不指定表名，默认会将大驼峰转换为：小写+下划线
#     # 如：类名UserModel => 表名user_model
#     # 指定表名，使用__tablename__属性
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(32), unique=True)
#     email = db.Column(db.String(64), unique=True)


class Apmuser(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    user_name =db.Column(db.String)
    user_nick = db.Column(db.String)

    def __init__(self,user_id,user_name,user_nick):
        self.user_id =user_id
        self.user_name =user_name
        self.user_nick = user_nick
    def __str__(self):
        return "id:{}--name:{}--nick:{}".format(self.user_id,self.user_name,self.user_nick)


class ApmTerms(db.Model):
    term_id = db.Column(db.BIGINT,primary_key=True)
    name =db.Column(db.String)
    slug = db.Column(db.String)
    term_group = db.Column(db.BIGINT)

    def __init__(self,term_id,name,slug,term_group):
        self.term_id =term_id
        self.name =name
        self.slug = slug
        self.term_group =term_group
    def __str__(self):
        return "term_id:{}--name:{}--slug{}--term_grop{}".format(self.term_id,self.name,self.slug,self.term_group)
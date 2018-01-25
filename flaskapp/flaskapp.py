# -*- coding: UTF-8 -*-
from flask import Flask,request,url_for,render_template
from models import User
app = Flask(__name__)


@app.route('/')
def hello_world():
    content= "this is template"
    return  render_template("index.html",content=content)

@app.route('/user',methods=['POST'])
def hello_user():
    return 'hello user'

@app.route('/user')
def user_index():
    user = User(1,'zhangjie')
    return  render_template("user_index.html",user=user)
@app.route('/query_users/<user_id>')
def query_users(user_id):
    users=None
    if int(user_id) == 1:
        users = User(1,'zhangjie')

    return render_template("user_id.html",users=users)

@app.route('/users/<id>')
def user_id(id):
    return 'hello user:'+id

@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return 'query user id:'+id
# 返乡路由
@app.route('/query_url')
def query_url():
    return 'query url:'+url_for('query_url')

@app.route('/users')
def user_list():
    users=[]
    for i in range(1,11):
        user =User(i,'zhangjie'+str(i))
        users.append(user)
    return  render_template("user_list.html",users=users)

@app.route('/one')
def one_base():
    return  render_template("one_base.html")

@app.route('/two')
def two_base():
    return  render_template("two_base.html")


if __name__ == '__main__':
    app.run()

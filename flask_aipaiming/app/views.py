from datetime import datetime

from flask import render_template, request,jsonify

from app.models import ApmUsers
from app import app

@app.route('/')
def index():
    user_logins = ApmUsers.objects.order_by('-user_registered')
    return render_template("index.html",user_logins=user_logins)

#Home
@app.route('/main/')
def mainpage():
    return  render_template("main.html")

#category
@app.route('/category/')
def category():
    return  render_template("category.html")
#me
@app.route('/me/')
def me():
    return  render_template("me.html")


#detail
@app.route('/detail/')
def detail():
    return  render_template("detail.html")



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
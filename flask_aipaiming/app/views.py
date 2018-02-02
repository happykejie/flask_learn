from datetime import datetime

from flask import render_template, request,jsonify
from flask_wtf import  form
from app.models import ApmUsers, ApmPosts
from app import app

@app.route('/')
def index():
    return  'test'

#Home
@app.route('/main/')
def mainpage():
    page = request.args.get('page', 1, type=int)
    pagination = ApmPosts.query.order_by(ApmPosts.post_date.desc()).paginate(page, per_page=10, error_out=False)
    apm_posts = pagination.query.all()
    return render_template('main.html', form=form, posts=apm_posts, pagination=pagination)

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
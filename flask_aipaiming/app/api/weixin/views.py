# coding: utf-8
from app.api import api
from flask import jsonify,request,json
from datetime import datetime
from app.models import ApmUsers,ApmTerms, ApmPosts
from flask_sqlalchemy import  SQLAlchemy

from app import  app

import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import datetime


def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    data = obj.__getattribute__(field)
                    try:
                        if isinstance(data, datetime):
                            data = data.strftime('%Y-%m-%d %H:%M:%S')
                        json.dumps(data)  # this will fail on non-encodable values, like other classes
                        fields[field] = data
                    except TypeError:
                        fields[field] = None
                return fields

            return json.JSONEncoder.default(self, obj)
    return AlchemyEncoder


user_data = [
    {
        'id': 1,
        'name': '张三',
        'age': 23
    },
    {
        'id': 2,
        'name': '李四',
        'age': 24
    }
]


@api.route('/weixin/user/<int:id>', methods=['GET', ])
def wx_user_get(id):
    for user in user_data:
        if user['id'] == id:
            return jsonify(status='success', user=user)


@api.route('/weixin/user/users', methods=['GET', ])
def wx_user_users():
    data = {
        'status': 'success',
        'users': user_data
    }
    return json.dumps(data, ensure_ascii=False, indent=1)


@api.route('/weixin/apm_posts',methods =['GET','POST'])
def query_apm_posts():
    page = request.args.get('page', 1, type=int)
    pagination = ApmPosts.query.order_by(ApmPosts.post_date.desc()).paginate(page, per_page=10, error_out=False)
    apm_posts = pagination.query.all()
    msgs = []
    for msg in apm_posts:

        jsonitme ={
            'post_author':msg.post_author,
            'post_content':msg.post_content,
            'post_title':msg.post_title,
            'post_status':msg.post_status
        }
        msgs.append(jsonitme)
    UnReadMsg = json.dumps(msgs, cls=new_alchemy_encoder(), check_circular=False,ensure_ascii=False)
    return UnReadMsg







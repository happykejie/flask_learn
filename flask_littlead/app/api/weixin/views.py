# coding: utf-8
from app.api import api
from flask import jsonify
import json
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
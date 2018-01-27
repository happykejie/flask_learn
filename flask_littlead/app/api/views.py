# coding: utf-8
from app.api import api
from flask import jsonify,make_response
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


from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

#region  web service access auth
@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

#endregion

@api.route('/user/<int:id>', methods=['GET', ])
@auth.login_required
def user_get(id):
    for user in user_data:
        if user['id'] == id:
            return jsonify(status='success', user=user)


@api.route('/user/users', methods=['GET', ])
def user_users():
    data = {
        'status': 'success',
        'users': user_data
    }
    return json.dumps(data, ensure_ascii=False, indent=1)
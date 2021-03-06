# coding:utf-8

from app.api import api
from flask import jsonify
import json

dept_data = [
    {
        'name': '部门1',
        'id': 12345
    },
    {
        'name': '部门2',
        'id': 12346
    }
]


@api.route('/dept/<int:id>', methods=['GET', ])
def dept_get(id):
    for dept in dept_data:
        if int(dept['id']) == id:
            return jsonify(status='success', dept=dept)


    return jsonify(status='failed', msg='dept not found')


@api.route('/dept/depts', methods=['GET', ])
def dept_get_depts():
    data = {
        'status': 'success',
        'depts': dept_data
    }
    return json.dumps(data, ensure_ascii=False, indent=1)
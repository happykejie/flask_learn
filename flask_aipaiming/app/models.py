import datetime

from flask_mongoengine.wtf import model_form

from app import db


class Todo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default = datetime.datetime.now())
    status = db.IntField(default = 0)


TodoForm = model_form(Todo)


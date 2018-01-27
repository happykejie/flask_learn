from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')

app.config['JSON_AS_ASCII'] = False

db = MongoEngine(app)

from app import views

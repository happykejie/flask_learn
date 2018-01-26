from flask import Flask
from flask_mongoengine import MongoEngine

api = Flask(__name__)
api.config.from_object('config')

db = MongoEngine(api)

from api import views

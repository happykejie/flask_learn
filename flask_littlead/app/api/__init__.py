# coding:utf-8
from flask import Blueprint

api = Blueprint('api',__name__)

from app.api import views
from app.api import deptapi

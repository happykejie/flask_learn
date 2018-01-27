# coding:utf-8
from flask import Blueprint

weixin = Blueprint('weixin',__name__)

from app.api.weixin import views

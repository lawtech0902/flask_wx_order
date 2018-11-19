# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/11/11 9:12 PM'
"""

from flask import Blueprint

route_api = Blueprint("api_page", __name__)

from web.controllers.api.member import *


@route_api.route("/")
def index():
    return "wx_app api v1.0~"

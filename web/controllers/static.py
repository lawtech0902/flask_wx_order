# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/27 3:31 PM'
解决加载静态资源问题
"""

from flask import Blueprint, send_from_directory
from application import app

route_static = Blueprint("static", __name__)


@route_static.route("/<path:filename>")
def index(filename):
    return send_from_directory(app.root_path + "/web/static/", filename)

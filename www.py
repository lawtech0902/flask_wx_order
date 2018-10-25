# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/24 8:46 PM'
HTTP模块相关初始化
"""

from application import app
from web.controllers.index import route_index

app.register_blueprint(route_index, url_prefix="/")

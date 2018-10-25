# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/25 8:52 PM'
"""

from flask import Blueprint

route_index = Blueprint('index_page', __name__)


@route_index.route('/')
def index():
    return "Hello World!"

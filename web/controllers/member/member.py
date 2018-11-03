# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/27 3:14 PM'
"""

from flask import Blueprint
from common.libs.helper import ops_render


route_member = Blueprint('member_page', __name__)


@route_member.route("/index")
def index():
    return ops_render("member/index.html")


@route_member.route("/info")
def info():
    return ops_render("member/info.html")


@route_member.route("/set")
def set():
    return ops_render("member/set.html")


@route_member.route("/comment")
def comment():
    return ops_render("member/comment.html")

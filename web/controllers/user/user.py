# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/27 3:14 PM'
"""

from flask import Blueprint, render_template

route_user = Blueprint('user_page', __name__)


@route_user.route("/login")
def login():
    return render_template("user/login.html")


@route_user.route("/edit")
def edit():
    return render_template("user/edit.html")


@route_user.route("/reset-pwd")
def reset_pwd():
    return render_template("user/reset_pwd.html")

# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/27 3:14 PM'
"""

from flask import Blueprint
from common.libs.helper import ops_render


route_finance = Blueprint('finance_page', __name__)


@route_finance.route("/index")
def index():
    return ops_render("finance/index.html")


@route_finance.route("/pay-info")
def payInfo():
    return ops_render("finance/pay_info.html")


@route_finance.route("/account")
def account():
    return ops_render("finance/account.html")

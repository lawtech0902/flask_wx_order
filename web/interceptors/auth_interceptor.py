# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/31 4:48 PM'
"""

from application import app
from flask import request, redirect, g
from common.models.user import User
from common.libs.user.user_service import UserService
from common.libs.log_service import LogService
from common.libs.url_manager import UrlManager

import re


@app.before_request
def before_request():
    ignore_urls = app.config["IGNORE_URLS"]
    ignore_check_login_urls = app.config["IGNORE_CHECK_LOGIN_URLS"]
    path = request.path

    # 如果是静态文件就不要查询用户信息了
    pattern = re.compile("{}".format("|".join(ignore_check_login_urls)))
    if pattern.match(path):
        return

    user_info = check_login()
    g.current_user = None
    if user_info:
        g.current_user = user_info

    # 加入日志
    LogService.add_access_log()

    pattern = re.compile("{}".format("|".join(ignore_urls)))
    if pattern.match(path):
        return

    if not user_info:
        return redirect(UrlManager.buildUrl("/user/login"))

    return


def check_login():
    """判断用户是否已经登录"""
    cookies = request.cookies
    auth_cookie = cookies[app.config["AUTH_COOKIE_NAME"]] if app.config["AUTH_COOKIE_NAME"] in cookies else None
    if not auth_cookie:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by(uid=auth_info[1]).first()
    except Exception:
        return False

    if not user_info:
        return False

    if auth_info[0] != UserService.gen_auth_code(user_info):
        return False

    if user_info.status != 1:
        return False

    return user_info

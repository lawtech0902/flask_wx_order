# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/24 8:44 PM'
"""

SERVER_PROT = 8999
DEBUG = False
SQLALCHEMY_ECHO = False
AUTH_COOKIE_NAME = "mooc_food"

# 过滤url
IGNORE_URLS = [
    "^/user/login",
    "^/api"
]
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

# 分页
PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1": "正常",
    "0": "删除"
}

# 小程序配置信息
WX_APP = {
    "app_id": "wx130f734f52af1c8a",
    "app_secret": "be32ac383def210a0dbc0072142be8f1"
}

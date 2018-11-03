# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/11/2 9:17 PM'
"""

from common.models.log.app_access_log import AppAccessLog
from common.models.log.app_error_log import AppErrorLog
from common.libs.helper import get_current_date
from flask import request, g
from application import db

import json


class LogService(object):

    @staticmethod
    def add_access_log():
        """添加访问记录"""
        target = AppAccessLog()
        target.target_url = request.url
        target.referer_url = request.referrer
        target.ip = request.remote_addr
        target.query_params = json.dumps(request.values.to_dict())
        if "current_user" in g and g.current_user is not None:
            target.uid = g.current_user.uid
        target.ua = request.headers.get("User-Agent")
        target.created_time = get_current_date()
        db.session.add(target)
        db.session.commit()
        return True

    @staticmethod
    def add_error_log(content):
        """添加错误记录"""
        if "favicon.ico" in request.url:
            return
        target = AppErrorLog()
        target.target_url = request.url
        target.referer_url = request.referrer
        target.query_params = json.dumps(request.values.to_dict())
        target.content = content
        target.created_time = get_current_date()
        db.session.add(target)
        db.session.commit()
        return True

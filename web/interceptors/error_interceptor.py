# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/11/3 10:15 PM'
"""

from application import app
from common.libs.helper import ops_render
from common.libs.log_service import LogService


@app.errorhandler(404)
def error_404(e):
    LogService.add_error_log(str(e))
    return ops_render("error/error.html", {"status": 404, "msg": "很抱歉！您访问的页面不存在"})

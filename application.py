# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/24 8:42 PM'
封装flask的全局变量，包括app，数据库连接等
"""

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

import os


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path,
                                          static_folder=None)
        self.config.from_pyfile('config/base_setting.py')
        if 'ops_config' in os.environ:
            self.config.from_pyfile('config/{}_setting.py'.format(os.environ['ops_config']))
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd() + "/web/templates/", root_path=os.getcwd())
manager = Manager(app)

'''
函数模板 ，即py文件中的静态方法，可以在html模板中调用 (如/common/layout_user.html", line 9)
'''
# 不要放在头部，避免循环引用问题
from common.libs.url_manager import UrlManager

app.add_template_global(UrlManager.buildStaticUrl, "buildStaticUrl")
app.add_template_global(UrlManager.buildUrl, "buildUrl")

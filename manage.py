# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/24 8:46 PM'
启动入口
"""

from application import app, manager
from flask_script import Server

import sys
import traceback
import www

# web
manager.add_command("runserver",
                    Server(host='0.0.0.0', port=app.config["SERVER_PROT"], use_debugger=True, use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()

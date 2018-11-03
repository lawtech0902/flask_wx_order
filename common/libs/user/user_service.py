# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/30 3:28 PM'
"""

import hashlib
import base64
import random
import string


class UserService(object):

    @staticmethod
    def gen_pwd(pwd, salt):
        m = hashlib.md5()
        str = "{}-{}".format(base64.encodebytes(pwd.encode("utf-8")), salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def gen_auth_code(user_info=None):
        m = hashlib.md5()
        str = "{}-{}-{}-{}".format(user_info.uid, user_info.login_name, user_info.login_pwd, user_info.login_salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def gen_salt(length=16):
        key_list = [random.choice(string.ascii_letters + string.digits) for _ in range(length)]
        return "".join(key_list)

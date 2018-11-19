# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/11/15 4:59 PM'
"""

from application import app

import random
import string
import hashlib
import json
import requests


class MemberService():

    @staticmethod
    def gen_auth_code(member_info=None):
        m = hashlib.md5()
        str = "{}-{}-{}".format(member_info.id, member_info.salt, member_info.status)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def gen_salt(length=16):
        key_list = [random.choice(string.ascii_letters + string.digits) for _ in range(length)]
        return "".join(key_list)

    @staticmethod
    def get_wx_openid(code):
        url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code".format(
            app.config["WX_APP"]["app_id"], app.config["WX_APP"]["app_secret"], code)
        r = requests.get(url)
        res = json.loads(r.text)
        openid = None
        if "openid" in res:
            openid = res["openid"]
        return openid

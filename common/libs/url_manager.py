# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/10/27 3:14 PM'
链接管理器
"""


class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver = "%s" % (22222222)
        path = "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl(path)

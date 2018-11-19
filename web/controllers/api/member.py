# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/11/14 3:17 PM'
"""

from flask import request, jsonify
from web.controllers.api import route_api
from application import app, db
from common.models.member.member import Member
from common.models.member.oauth_member_bind import OauthMemberBind
from common.libs.helper import get_current_date
from common.libs.member.member_service import MemberService


@route_api.route("/member/login", methods=["GET", "POST"])
def login():
    resp = {"code": 200, "msg": "操作成功", "data": {}}
    req = request.values
    code = req["code"] if "code" in req else ""
    if not code or len(code) < 1:
        resp["code"] = -1
        resp["msg"] = "需要code"
        return jsonify(resp)

    openid = MemberService.get_wx_openid(code)
    if openid is None:
        resp["code"] = -1
        resp["msg"] = "调用微信出错"
        return jsonify(resp)

    nickname = req["nickName"] if "nickName" in req else ""
    sex = req["gender"] if "gender" in req else 0
    avatar = req["avatarUrl"] if "avatarUrl" in req else ""

    # 判断是否已经测试过，注册了直接返回一些信息
    bind_info = OauthMemberBind.query.filter_by(openid=openid, type=1).first()
    if not bind_info:
        model_member = Member()
        model_member.nickname = nickname
        model_member.sex = sex
        model_member.avatar = avatar
        model_member.salt = MemberService.gen_salt()
        model_member.updated_time = model_member.created_time = get_current_date()
        db.session.add(model_member)
        db.session.commit()

        model_bind = OauthMemberBind()
        model_bind.member_id = model_member.id
        model_bind.type = 1
        model_bind.openid = openid
        model_bind.extra = ""
        model_bind.updated_time = model_bind.created_time = get_current_date()
        db.session.add(model_bind)
        db.session.commit()

        bind_info = model_bind

    member_info = Member.query.filter_by(id=bind_info.member_id).first()
    token = "{}#{}".format(MemberService.gen_auth_code(member_info), member_info.id)
    resp["data"] = {"token": token}
    return jsonify(resp)


@route_api.route("/member/check-reg", methods=["GET", "POST"])
def check_reg():
    resp = {"code": 200, "msg": "操作成功", "data": {}}
    req = request.values
    code = req["code"] if "code" in req else ""
    if not code or len(code) < 1:
        resp["code"] = -1
        resp["msg"] = "需要code"
        return jsonify(resp)

    openid = MemberService.get_wx_openid(code)
    if openid is None:
        resp["code"] = -1
        resp["msg"] = "调用微信出错"
        return jsonify(resp)

    bind_info = OauthMemberBind.query.filter_by(openid=openid, type=1).first()
    if not bind_info:
        resp['code'] = -1
        resp['msg'] = "未绑定"
        return jsonify(resp)

    member_info = Member.query.filter_by(id=bind_info.member_id).first()
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "未查询到绑定信息"
        return jsonify(resp)

    token = "{}#{}".format(MemberService.gen_auth_code(member_info), member_info.id)
    resp["data"] = {"token": token}
    return jsonify(resp)

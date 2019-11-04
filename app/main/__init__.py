# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from app.main.blue_print import Hello_v1, Hello_v2


# 注册蓝图
# 创建蓝图
def create_blueprint_v1():
    """
    注册蓝图->v1版本
    """
    bp_v1 = Blueprint('v1', __name__)
    register_views(bp_v1)
    return bp_v1


def create_blueprint_v2():
    """
    注册蓝图->v2版本
    """
    bp_v2 = Blueprint('v2', __name__)
    register_views_v2(bp_v2)
    return bp_v2


# restful api
def register_views(app):
    api = Api(app)
    api.add_resource(Hello_v1, '/hello_v1', endpoint="hello_v1")


# restful api
def register_views_v2(app):
    api = Api(app)
    api.add_resource(Hello_v2, '/hello_v2', endpoint="hello_v2")

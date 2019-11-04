# -*- coding: utf-8 -*-
# 在apps中init
from app.main import create_blueprint_v1, create_blueprint_v2


# 把刚才注册的蓝点路由，注册到程序的主入口文件中
# 引入蓝图
def register_blueprints(app):
    # 注册蓝图v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')
    # 注册蓝图v2
    app.register_blueprint(create_blueprint_v2(), url_prefix='/v2')

from flask import Flask
# 引入蓝图
from app import register_blueprints
# log
from app.controller.logger import log
import os
from datetime import timedelta
import configparser
_app = Flask(__name__)

# # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
# _app.config['SECRET_KEY'] = os.urandom(24)
#
# # 设置session的保存时间。
# _app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)


# 项目启动
def init_app(app):
    # 插入配置文件,设置全局config配置文件
    # config 地址在创建docker镜像之前需要修改
    cf = configparser.ConfigParser()
    cf.read('./config.ini')
    _app.config['config'] = cf
    # 创建log文件
    log.initialize()
    log_file = cf.get("Log", "log_file")
    log.set_attribute(console=True, filename=log_file)
    # 引入蓝图路由
    register_blueprints(app)


init_app(_app)

if __name__ == '__main__':
    _app.run(
        host='0.0.0.0',
        port=5000,
        threaded=True,
        debug=True
    )

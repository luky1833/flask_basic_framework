from flask import Flask
# 引入蓝图
from app import register_blueprints

_app = Flask(__name__)


# 引入蓝图路由
def init_app(app):
    register_blueprints(app)


init_app(_app)

if __name__ == '__main__':
    _app.run(
        # host='0.0.0.0',
        port=5000,
        threaded=True,
        debug=True
    )

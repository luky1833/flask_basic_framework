# -*- coding: utf-8 -*-
from flask import Flask

_app = Flask(__name__)


@_app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    _app.run()

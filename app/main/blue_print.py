# -*- coding: utf-8 -*-
from flask_restful import Resource


class Hello_v1(Resource):
    def __init__(self):
        pass

    def get(self):
        return 'hello 111!'


class Hello_v2(Resource):
    def __init__(self):
        pass

    def get(self):
        return 'hello 222!'

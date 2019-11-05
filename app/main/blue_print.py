# -*- coding: utf-8 -*-
from flask import current_app
from flask_restful import Resource, reqparse
from app.controller.logger import log


class Hello_v1(Resource):
    def __init__(self):
        # 设置参数
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('key1', type=int)
        self.parser.add_argument('key2', type=int)
        pass

    def get(self):
        try:
            # get 获取参数
            cf = current_app.config['config']
            client_cert = cf.get("ES", "client_cert")
            data = self.parser.parse_args()
            value1 = data.get('key1')
            value2 = data.get('key2')
            return 'hello 111!'
        except Exception as e:
            
            log.e('blue_print.Hello_v1.get:' + str(e) + '\n')
            error = dict()
            error['error_503'] = str(e)
            # return self.write_json(500, '获取参数失败')
            return 1,500

    def post(self):
        # post 获取参数
        args = self.parser.parse_args()
        return args['key1'], 200


class Hello_v2(Resource):
    def __init__(self):
        pass

    def get(self):
        return 'hello 222!'

# -*- coding: utf-8 -*-
import binascii
import os
import json
import time
from concurrent.futures import ThreadPoolExecutor
from flask_restful import Resource
from app.utils.CJsonEncoder import CJsonEncoder

class SwxJsonHandler(Resource):
    """
    所有返回JSON数据的控制器均从本类集成，返回的数据格式一律包含三个字段：code/msg/data
    code: 0=成功，其他=失败
    msg: 字符串，一般用于code为非零时，指出错误原因
    data: 一般用于成功操作的返回的业务数据
    """
    executor = ThreadPoolExecutor(max_workers=10)  # 全局线程池

    def __init__(self):
        super().__init__()

    def write_json(self, code, message='', data=None):
        if not isinstance(code, int):
            raise RuntimeError('`code` must be a integer.')
        if not isinstance(message, str):
            raise RuntimeError('`msg` must be a string.')

        if data is None:
            data = list()

        _ret = {'code':code, 'message':message, 'data':data}
        return _ret

    # def write_json_msg(self, code, message='', data=None):
    #     if not isinstance(code, int):
    #         raise RuntimeError('`code` must be a integer.')
    #     if not isinstance(message, str):
    #         raise RuntimeError('`msg` must be a string.')
    #
    #     if data is None:
    #         data = list()
    #     _ret = {'code':code, 'msg':message, 'data':data}
    #
    #     self.write(json.dumps(_ret, cls=CJsonEncoder))
    #
    # def write_json_msg_html(self, code, message='', data=None):
    #     if not isinstance(code, int):
    #         raise RuntimeError('`code` must be a integer.')
    #     if not isinstance(message, str):
    #         raise RuntimeError('`msg` must be a string.')
    #
    #     if data is None:
    #         data = list()
    #
    #     _ret = {'code':code, 'msg':message, 'data':data}
    #
    #     self.write(json.dumps(_ret, cls=CJsonEncoder))
    #
    # def write_raw_json(self, data=None):
    #     if data is None:
    #         data = list()
    #
    #     self.write(json.dumps(data, cls=CJsonEncoder))

# 单元测试
import unittest

import requests
from app.controller.logger import log
import json


class web_requests(unittest.TestCase):
    def get(self, url, params=None, headers=None, files=None):
        # '''封装get方法，return响应码和响应内容'''
        try:
            r = requests.get(url, params=params, headers=headers, files=files)
            log.e("请求的内容：%s" % params)
            status_code = r.status_code  # 获取返回的状态码
            log.e("获取返回的状态码:%d" % status_code)
            response_json = r.json()  # 响应内容，json类型转化成python数据类型
            log.e("响应内容：%s" % response_json)
            return status_code, response_json  # 返回响应码，响应内容
        except BaseException as e:
            log.e("请求失败！", exc_info=1)

    def post(self, url, data=None, headers=None, files=None):
        # '''封装post请求，return响应码和响应内容'''
        try:
            r = requests.post(url, data=data, headers=headers, files=files)
            log.e("请求的内容：%s" % data)
            status_code = r.status_code  # 获取返回的状态码
            log.e("获取返回的状态码:%d" % status_code)
            response_json = r.json()  # 响应内容，json类型转化成python数据类型
            log.e("响应内容：%s" % response_json)
            return status_code, response_json  # 返回响应码，响应内容
        except BaseException as e:
            log.e("请求失败！", exc_info=1)

    def post_json(self, url, data=None, headers=None):
        # '''封装post方法，并用json格式传值，return响应码和响应内容'''
        try:
            data = json.dumps(data).encode('utf-8')  # python数据类型转化为json数据类型
            r = requests.post(url, data=data, headers=headers)
            log.e("请求的内容：%s" % data)
            status_code = r.status_code  # 获取返回的状态码
            log.e("获取返回的状态码:%d" % status_code)
            response = r.json()  # 响应内容，json类型转化成python数据类型
            log.e("响应内容：%s" % response)
            return status_code, response  # 返回响应码，响应内容
        except BaseException as e:
            log.e("请求失败！", exc_info=1)

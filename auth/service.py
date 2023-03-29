# coding=utf-8
# @Author:zcl01
# @Create_time:2023/3/23 18:49
# @File_name:service

# 创建请求处理器
# 当处理请求时会进行实例化并调用HTTP请求对应的方法
import traceback
from typing import Optional, Awaitable

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        try:
            # 从querystring查询字符串中获取id参数的值，若无则默认为0.
            _id = self.get_argument("id", 0)
            if id:
                # write方法将字符串写入HTTP响应
                self.write("hello world id = " + _id)
            else:
                self.write("id is not found")
        except Exception as e:
            self.write(traceback.format_exc())

    def post(self):
        _id = self.get_body_argument("id")
        self.write({"_id": _id})


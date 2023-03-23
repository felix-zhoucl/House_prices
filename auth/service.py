# coding=utf-8
# @Author:zcl01
# @Create_time:2023/3/23 18:49
# @File_name:service

# 创建请求处理器
# 当处理请求时会进行实例化并调用HTTP请求对应的方法
import traceback

import tornado


class IndexHandler(tornado.web.RequestHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        print(self.cookies)
        try:
            # 从querystring查询字符串中获取id参数的值，若无则默认为0.
            id = self.get_argument("id", 0)
            if id:
                # write方法将字符串写入HTTP响应
                self.write("hello world id = " + id)
            else:
                self.write("id is not found")
        except Exception as e:
            self.write(traceback.format_exc())

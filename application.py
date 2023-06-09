# coding=utf-8
# @Author:zcl01
# @Create_time:2023/3/20 16:16
# @File_name:application
# ! /usr/bin/python
# encoding:utf-8
import logging

import tornado.httpserver  # 异步非阻塞HTTP服务器模块
import tornado.ioloop  # 核心IO循环模块
import tornado.options  # 解析终端参数模块
import tornado.web  # Web框架模块
# 从终端模块中导出define模块用于读取参数，导出options模块用于设置默认参数
from tornado.options import define, options

import auth.service
from environment import print_log

# 定义端口用于指定HTTP服务监听的端口
# 如果命令行中带有port同名参数则会称为全局tornado.options的属性，若没有则使用define定义。
define("port", type=int, default=8000, help="run on the given port")

# 创建路由表
urls = [(r"/", auth.service.IndexHandler), ]


# 定义服务器
def main():
    print_log('run.log')
    # 解析命令行参数
    tornado.options.parse_command_line()
    # 创建应用实例
    app = tornado.web.Application(urls)
    # 监听端口
    app.listen(options.port)
    logging.info("server started on port：%s", 8000)
    # 创建IOLoop实例并启动
    tornado.ioloop.IOLoop.current().start()


# 应用运行入口，解析命令行参数
if __name__ == "__main__":
    # 启动服务器
    main()

# coding=utf-8
# @Author:zcl01
# @Create_time:2023/3/20 16:18
# @File_name:environment
import json
import logging
import os
import traceback

import dbutils.pooled_db as pool_db
import pymysql

"""输出日志到控制台和文件"""
LOG_PATH = './log/'
LOG_LEVEL = logging.DEBUG


# LOG_LEVEL = logging.INFO


def get_config(key, path=None):
    """
    读取配置文件信息
    :param path:
    :param key:
    :return:
    """
    if not path:
        path = "config.json"
    try:
        with open(path, "r", encoding="GBK") as f:
            ret = json.load(f)
            key_list = key.split(".")
            for key_ in key_list:
                ret = ret.get(key_)
            return ret
    except:
        logging.error(traceback.format_exc())


def db():
    """
    链接数据库
    :return:
    """
    pool = pool_db.PooledDB(
        creator=pymysql,  # 使用链接数据库的模块
        maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
        mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
        blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
        ping=0,
        host=get_config("__db_host__"),
        port=get_config("__db_port__"),
        user=get_config("__db_user__"),
        password=get_config("__db_pwd__"),
        database=get_config("__db_name__"),
        charset='utf8'
    )
    return pool.connection()


def print_log(logFilename, log_level=None):
    """
    记录日志文件并输出到控制台
    :param log_level: 日志级别
    :param logFilename: 日志文件名称
    :return:
    """
    # 判断目录是否存在
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)

    """输出到文件的设置"""
    logging.basicConfig(
        level=logging.DEBUG,  # 定义输出到文件的log级别，大于此级别的都被输出
        format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
        datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
        filename='./log/' + logFilename,  # log文件存储位置+文件名
        filemode='a+')  # 文件读写模式 a+为追加写
    """输出到控制台的句柄"""
    console = logging.StreamHandler()
    if log_level:
        console.setLevel(log_level)
    else:
        console.setLevel(LOG_LEVEL)  # 定义输出到文件的log级别，大于此级别的都被输出
    formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义输出log的格式
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

# coding=utf-8
# @Author:zcl01
# @Create_time:2023/3/20 16:18
# @File_name:environment
import logging
import os

"""全局变量"""
LOG_PATH = './log/'
LOG_LEVEL = logging.DEBUG

"""输出日志到控制台和文件"""


def print_log(logFilename):
    """
    记录日志文件并输出到控制台
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
    console.setLevel(LOG_LEVEL)  # 定义输出到文件的log级别，大于此级别的都被输出
    formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义输出log的格式
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

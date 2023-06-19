# coding=utf-8
# @Author:Felix
# @Create_time:2023/6/13 16:46
# @File_name:test


# des:给定一个list 其中元素为dict，要求输出list中所有元素的name字段值
# 输入：
origin_list = [
    {"name": "test1", "score": 10, "create_time": "2022-11-13 12:00:00"},
    {"name": "test2", "score": 20, "create_time": "2022-11-12 12:00:00"},
    {"name": "test3", "score": 30, "create_time": "2022-11-11 12:00:00"},
    {"name": "test4", "score": 40, "create_time": "2022-11-11 11:00:00"},
    {"name": "test4", "score": 40, "create_time": "2022-11-10 12:00:00"},
    {"name": "test4", "score": 40, "create_time": "2022-11-10 12:00:00"}
]
# 输出1 所有元素的name值（要求去重）
ret = ["test1", "test2", "test3", "test4"]
# 输出2 去重排序后的原始列表，要求按照score，create_time 降序排序，score优先
ret2 = [{'name': 'test4', 'score': 40, 'create_time': '2022-11-11 11:00:00'},
        {'name': 'test4', 'score': 40, 'create_time': '2022-11-10 12:00:00'},
        {'name': 'test3', 'score': 30, 'create_time': '2022-11-11 12:00:00'},
        {'name': 'test2', 'score': 20, 'create_time': '2022-11-12 12:00:00'},
        {'name': 'test1', 'score': 10, 'create_time': '2022-11-13 12:00:00'}]
# 输出3 给定另一个列表tel_list，要求按照name去匹配数据，带出对应人员的手机号（cell），查询不到则为None，
# 要求效率要高，时间复杂度优先,返回处理后的原始数据
tel_list = [
    {"name": "test1", "cell": "17812312345"},
    {"name": "test2", "cell": "17812312346"},
    {"name": "test3", "cell": "17812312347"}
]
ret3 = [
    {"name": "test1", "score": 10, "create_time": "2022-11-13 12:00:00", "cell": "17812312345"},
    {"name": "test2", "score": 20, "create_time": "2022-11-12 12:00:00", "cell": "17812312346"},
    {"name": "test3", "score": 30, "create_time": "2022-11-11 12:00:00", "cell": "17812312347"},
    {"name": "test4", "score": 40, "create_time": "2022-11-11 11:00:00", "cell": None},
    {"name": "test4", "score": 40, "create_time": "2022-11-10 12:00:00", "cell": None},
    {"name": "test4", "score": 40, "create_time": "2022-11-10 12:00:00", "cell": None}
]

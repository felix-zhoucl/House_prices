# coding=utf-8
# @Author:zcl01
# @Create_time:2023/4/17 19:15
# @File_name:Ekb
import json

import requests

from environment import db

SID = "renzhi"
USERNAME = "15014125325"
PASSWORD = "Aa123456789"


def get_session():
    """获取登录session"""
    login_url = "https://erp.ekbyun.com/index.php/home/login/access.html"
    session_ = requests.Session()
    payload = {
        'data': '{"sid":"renzhi","username":"15014125325","password":"3d558122fcac9ea5fdc9ee8eccf8f433"}'
    }
    response_ = session_.post(login_url, data=payload)
    result_ = json.loads(response_.text)
    return session_


def get_list_data(session_, index_, page_size):
    """
    分页取数
    :param session_:session
    :param index_: 页数
    :param page_size: 每页大小
    :return:
    """
    url = "https://erp.ekbyun.com/index.php/trade/original_trade/getoriginaltradelist.html?process_status="

    payload = {
        'page': index_,
        'rows': page_size,
        'sort': 'trade_time',
        'order': 'asc',
        'search[shop_id]': '1'
    }
    response = session_.post(url, data=payload)
    ret = json.loads(response.text)
    return ret.get("rows")


def get_data(session_, p_id):
    """
    获取用户信息
    :param session_:
    :param p_id:
    :return:
    """
    url = "https://erp.ekbyun.com/index.php/trade/trade_common/getsensitivedata.html"
    payload = {
        'field': "receiver_mobile",
        'key': "apiTrade",
        'id': p_id,
        "platform_id": 0,
        'client_decrypt': 1
    }
    response = session_.post(url, data=payload)
    ret = json.loads(response.text)
    success = ret.get("message")
    if success == "success":
        return ret.get("success_response", {}).get("data")
    else:
        return {}


if __name__ == '__main__':
    print("fetch_begin")
    session = get_session()
    print("get_session")
    list_data = get_list_data(session, 1, 100)
    ids = [x.get("id") for x in list_data]
    print("get_list")
    conn = db()
    cursor = conn.cursor()
    print("conn_db")
    for id_ in ids:
        result = get_data(session, id_)
        if result:
            insert_sql = "INSERT INTO `mypf` (`receiver_address`, `receiver_mobile`, `receiver_name`, `receiver_telno`, `id`) " \
                         "VALUES ('{}', '{}', '{}', '{}', NULL);".format(result.get("receiver_address"),
                                                                         result.get("receiver_mobile"),
                                                                         result.get("receiver_name"),
                                                                         result.get("receiver_telno"))
            cursor.execute(insert_sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("success!!")

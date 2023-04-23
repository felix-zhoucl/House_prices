# coding=utf-8
# @Author:zcl01
# @Create_time:2023/4/17 19:15
# @File_name:Ekb
import json
import traceback

import requests

from environment import db

# SID = "renzhi"
# USERNAME = "15014125325"
# PASSWORD = "Aa123456789"
# password = "3d558122fcac9ea5fdc9ee8eccf8f433"
SID = "renzhi"
USERNAME = "admin"
PASSWORD = "Qwe12345678"
password = "89a4b59d1f657c9da72d94f797a55edf"


def get_session():
    """获取登录session"""
    login_url = "https://erp.ekbyun.com/index.php/home/login/access.html"
    session_ = requests.Session()
    # payload = {
    #     'data': '{"sid":"renzhi","username":"15014125325","password":"3d558122fcac9ea5fdc9ee8eccf8f433"}'
    # }
    payload = {
        'data': '{"sid":"renzhi","username":"admin","password":"89a4b59d1f657c9da72d94f797a55edf"}'
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
    # print(response.text)
    ret = json.loads(response.text)
    return ret.get("rows")


def check_verify_code(data_id):
    """
    识别验证码
    :return:
    """
    import ddddocr
    ocr = ddddocr.DdddOcr()
    # TODO:
    # 1获取验证码图片
    # 2保存本地
    with open('./verify_code/{}.png'.format(data_id), 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    print("识别验证码结果：{}".format(res))
    return res


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
        print(ret)
        return {}
        check_verify_code(data_id=p_id)
        ret = get_data(session_, p_id)
        if ret:
            return ret
        else:
            return {}


if __name__ == '__main__':
    print("fetch_begin")
    session = get_session()
    print("get_session")
    list_data = get_list_data(session, 5, 50)
    ids = [x.get("id") for x in list_data]
    print("get_list")
    conn = db()
    cursor = conn.cursor()
    print("conn_db")
    try:
        count = 0
        for id_ in ids:
            count += 1
            print("get:{}/50".format(count))
            result = get_data(session, id_)
            if result:
                insert_sql = "INSERT INTO `mypf` (`receiver_address`, `receiver_mobile`, `receiver_name`, `receiver_telno`, `id`,`data_id`) " \
                             "VALUES ('{}', '{}', '{}', '{}', NULL,'{}');".format(result.get("receiver_address"),
                                                                                  result.get("receiver_mobile"),
                                                                                  result.get("receiver_name"),
                                                                                  result.get("receiver_telno"),
                                                                                  id_)
                cursor.execute(insert_sql)
    except Exception as e:
        print(traceback.format_exc())
    finally:
        conn.commit()
        cursor.close()
        conn.close()
        print("success!!")

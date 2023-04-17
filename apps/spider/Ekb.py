# coding=utf-8
# @Author:zcl01
# @Create_time:2023/4/17 19:15
# @File_name:Ekb
import json

import requests

SID = "renzhi"
USERNAME = "15014125325"
PASSWORD = "Aa123456789"


def get_session():
    """获取登录session"""
    login_url = "https://erp.ekbyun.com/index.php/home/login/access.html"
    session_ = requests.Session()
    payload = {
        'data': '{"sid":"{}","username":"{}","password":"3d558122fcac9ea5fdc9ee8eccf8f433"}'.format(SID, USERNAME)
    }
    response_ = session_.post(login_url, data=payload)
    result_ = json.loads(response_.text)
    print(result_)
    return session_


if __name__ == '__main__':
    index = "https://erp.ekbyun.com/index.php"
    session = get_session()
    result = session.get(index)
    print(result.text)


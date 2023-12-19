# coding=utf-8
import urllib
import urllib.request
import hashlib

from environment import get_config


def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()


def send_SMS():
    statusStr = {
        '0': '短信发送成功',
        '-1': '参数不全',
        '-2': '服务器空间不支持,请确认支持curl或者fsocket,联系您的空间商解决或者更换空间',
        '30': '密码错误',
        '40': '账号不存在',
        '41': '余额不足',
        '42': '账户已过期',
        '43': 'IP地址限制',
        '50': '内容含有敏感词'
    }
    sms_api = "http://api.smsbao.com/"
    path = "../../config.json"
    # 短信平台账号
    user = get_config("sms.username", path)
    # 短信平台密码
    password = get_config("sms.password", path)
    # 要发送的短信内容
    content = '短信内容'
    # 要发送短信的手机号码
    phone = '15376666032'

    data = urllib.parse.urlencode({'u': user, 'p': password, 'm': phone, 'c': content})
    send_url = sms_api + 'sms?' + data
    response = urllib.request.urlopen(send_url)
    the_page = response.read().decode('utf-8')
    print(statusStr[the_page])


if __name__ == '__main__':
    send_SMS()

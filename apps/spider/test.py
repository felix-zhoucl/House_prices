# coding=utf-8
# @Author:zcl01
# @Create_time:2023/4/23 18:26
# @File_name:test
import requests
import wget


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


def check_verify_code(data_id, session_):
    """
    识别验证码
    :return:
    """
    import ddddocr
    ocr = ddddocr.DdddOcr()
    # 1获取验证码图片保存本地
    download_pic(data_id)
    # 2ocr识别
    with open('./verify_code/{}.png'.format(data_id), 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    print("data_id:{}识别验证码结果:{}".format(data_id, res))
    # 3验证验证码
    check_url = "https://erp.ekbyun.com/index.php/trade/trade_common/verifyimgcode.html"
    payload = {
        'code_type': 'get_sensitive_data',
        'verify_code': res
    }
    response = session_.post(check_url, data=payload)
    print(response)


def download_pic(data_id):
    """
    下载图片
    :param data_id:
    :return:
    """
    url = ""
    path = "./verify_code/{}.png".format(data_id)
    wget.download(url, path)


if __name__ == '__main__':
    # session = get_session()
    # data_id = 1234
    # download_pic(data_id)
    # check_verify_code(data_id, session)
    url="https://erp.ekbyun.com/index.php/trade/trade_common/showverifyimgcode.html?_=1682596470358"
    path="./1.html"
    wget.download(url, path)

# coding=utf-8
# @Author:zcl01
# @Create_time:2023/9/6 10:09
# @File_name:ImageUtils
import base64
import uuid


def save_image_base64(base64_str):
    """
    保存base64进制图片
    :param base64_str:
    :return:
    """
    bin_data = base64.b64decode(base64_str)
    filename = "{}.jpg".format(uuid.uuid4())
    file = open(filename, 'wb')
    file.write(bin_data)
    file.close()
    return filename


if __name__ == '__main__':
    img_str = ""
    save_image_base64(img_str)

# coding=utf-8
# @Author:zcl01
# @Create_time:2023/4/19 20:00
# @File_name:check_verify_code


# 图片处理
# 二值化处理 灰度阈值设为127，高于这个值的点全部填白色
from PIL import Image

img_old = Image.open('./verify_code/code.png')
img_old = img_old.convert('L')  # 灰度图 模式“L” 每个像素用8个bit表示，0表示黑，255表示白
threshld = 127  # 设置阈值，图片的像素范围（0，255）
table = []
for i in range(256):
    if i < threshld:
        table.append(0)
    else:
        table.append(1)
img_old = img_old.point(table, '1')  # 对图像像素操作 模式“1” 为二值图像，非黑即白。但是它每个像素用8个bit表示，0表示黑，255表示白
img_old.save('./verify_code/code.jpg')

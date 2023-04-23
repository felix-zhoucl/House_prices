# coding=utf-8
# @Author:zcl01
# @Create_time:2023/4/23 18:26
# @File_name:test
import ddddocr

ocr = ddddocr.DdddOcr()
with open('./verify_code/xarn.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
print(res)

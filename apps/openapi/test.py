# coding=utf-8
# @Author:zcl01
# @Create_time:2023/6/5 10:45
# @File_name:test
import get_chinese_number

if __name__ == '__main__':
    number = 123.22
    cn_math = get_chinese_number.GetChineseNumber()
    result = cn_math.execute(number)
    print(result)

# coding=utf-8
# @Author:zcl01
# @Create_time:2023/3/25 12:00
# @File_name:test

from environment import db

if __name__ == '__main__':
    conn = db()
    cursor = conn.cursor()
    # Unicode编码中文字符串：
    # reg="^[u4e00-u9fa5]$"
    reg = "[、-兼]"
    sql = "SELECT name FROM user WHERE name regexp '{}'".format(reg)
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()

# coding=utf-8
# @Author:zcl01
# @Create_time:2023/3/25 12:00
# @File_name:test

from environment import connect_db

if __name__ == '__main__':
    conn = connect_db().connection()
    cursor = conn.cursor()
    cursor.execute('select * from user')
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()

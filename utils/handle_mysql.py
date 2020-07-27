# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 10:52
# @Author  : Fighter
import pymysql
test_db_config={"host":"172.16.1.107","port":3306,"user":"qst","password":"Ast4HS#qianshitong","database":"u2s_traffic"}
connect = pymysql.Connect(**test_db_config)
def get_cursor(connect):
    return connect.cursor()

def select(connect,sql):
    try:
        cursor = get_cursor(connect)
        cursor.execute(sql)
        data =cursor.fetchall()
        cursor.close()
        return data
    except Exception as e:
        print(e)

if __name__ == '__main__':
    sql=f'''SELECT * FROM `vsd_task_info` LIMIT 0, 1000'''
    data=select(connect,sql)
    print(data)



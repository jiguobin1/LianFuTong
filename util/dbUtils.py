# -*- coding: utf-8 -*- 
# @Time : 2019/7/13 12:08 
# @Author : Ji
# @File : dbUtils.py 
import sqlite3
class dbUtils():
    conn=''
    cursor=''
    def __init__(self):
        pass

    #链接库/创建库
    def create(self,file):
        self.conn=sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    #执行sql
    def execute(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def close(self):
        #先关闭游标再关闭数据库链接
        self.cursor.close()
        self.conn.close()


# if __name__ == '__main__':
#     db=dbutils()
#     db.create('D:/mysql.db')
#     sql="CREATE TABLE op (type CHAR(20),Remarks CHAR(20),len INT,rows INT)"
#     db.execute(sql)
#     db.close()

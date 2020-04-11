# -*- coding: utf-8 -*-
"""

=================================
Author: yangli
Created on: 2020/3/15

E-mail:1179384105@qq.com

=================================


"""


import pymysql
from common.config import conf


class ExecuteMsql(object):
    def __init__(self):
        # 连接数据库
        self.con = pymysql.connect(
            host=conf.get("mysql", "host"),
            # 端口号必须为整型int
            port=conf.getint("mysql", "port"),
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "password"),
            database=conf.get("mysql", "database"),
            charset="utf8"
        )
        # 创建游标，通过游标来查询sql语句
        self.cur = self.con.cursor()

    # 查询一条结果，没有返回None，有多条数据只返回第一条
    def find_one(self, sql):
        # 执行sql语句
        self.cur.execute(sql)
        # 刷新数据并返回查询结果
        self.con.commit()
        return self.cur.fetchone()

    # 传入数字，查询符合条件的结果，从前往后只取指定数字个数的结果，没有返回空元组
    def find_many(self, sql, num):
        # 执行sql语句
        self.cur.execute(sql)
        # 刷新数据并返回查询结果
        self.con.commit()
        return self.cur.fetchmany(num)

    # 查询全部结果，没有返回空元组
    def find_all(self, sql):
        # 执行sql语句
        self.cur.execute(sql)
        # 刷新数据并返回查询结果
        self.con.commit()
        return self.cur.fetchall()

    # 查询个数，没有返回0
    def find_count(self, sql):
        count = self.cur.execute(sql)
        # 刷新数据并返回查询结果
        self.con.commit()
        return count



if __name__ == '__main__':
    sql = 'SELECT id FROM member WHERE RegName = "tudout"'
    s = ExecuteMsql()
    # res = s.find_one(sql)
    # res = s.find_many(sql, 3)
    # res = s.find_all(sql)
    res = s.find_count(sql)
    print(res)



# -*- coding: UTF-8 -*-


import pymysql
from tornado_template.Settings.ai_config import ai_config


class SQLManager(object):
    # 连接数据库
    # 将conn,cursor作为类的属性，通过connect方法触发生成
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect()

    def __del__(self):
        self.close()

    def connect(self):
        self.conn = pymysql.connect(
            host=ai_config.ip,
            port=ai_config.port,
            user=ai_config.username,
            password=ai_config.dbpwd,
            db=ai_config.dbname,
            charset=ai_config.charset
        )
        # 链接mysql
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 注意这种方式链接数据库，查询结果返回的是字典

    # 查询所有数据，传入的参数要是元组形式
    def many_query(self, sql, *args):
        try:
            self.cur.execute(sql, *args)
            print('数据库操作成功！')
            return self.cur.fetchall()
        except Exception as e:
            print('数据库查询失败！\n' + str(e))
            return False

    # 查询单条数据
    def single_query(self, sql, *args):
        try:
            # print(sql)
            # print(args)
            self.cur.execute(sql, *args)
            print('数据库操作成功！')
            return self.cur.fetchone()
        except Exception as e:
            print('数据库操作失败！\n' + str(e))
            return False

    # 单条增删改数据,创建表
    def modify(self, sql, *args):
        try:
            # print(args)
            self.cur.execute(sql, *args)  # 修改，由arge改为*args
            self.conn.commit()
            print('数据库操作成功！')
            return True
        except Exception as e:
            print('数据库操作失败！\n' + str(e))
            return False

    # 批量增加数据
    def many_insert(self, sql, data):
        try:
            self.cur.executemany(sql, data)
            self.conn.commit()
            print('数据库操作成功！')
            return True
        except Exception as e:
            print('数据库操作失败！\n' + str(e))
            return False

    # 关闭数据库cursor和连接
    def close(self):
        self.cur.close()
        self.conn.close()
        print('数据库成功断开链接！')
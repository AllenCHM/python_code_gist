#coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: 数据类型测试.py
@datetime: 2019-2-19 10:30
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


import pymysql

db = pymysql.connect("192.168.0.186","root","Nash1234@","allen")
cursor = db.cursor()
sql = "select * from tutorials_tbl"
cursor.execute(sql)
results = cursor.fetchall()

for row in results:
    for i in row:
        print i,

db.close()
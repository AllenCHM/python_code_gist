#coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: mont.py
@datetime: 2018-4-2 15:25
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import pymysql

import pymysql
import time
import datetime
conn = pymysql.Connection(host='192.168.0.186', port=3306, user='root', password='Nash1234@',
                          charset='utf8', db='test', autocommit=True)

tmp = 0
while True:
    with conn.cursor() as cursor:
        cursor.execute('SELECT count(*) from test_update')
        print(id(cursor))

        num = cursor.fetchall()
        if num[0][0] != tmp:
            print datetime.datetime.now(), num[0][0]
            tmp = num[0][0]
    time.sleep(10)



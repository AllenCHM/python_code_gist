#coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: myapp.py
@datetime: 3/11/2019 10:58 AM
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from datetime import datetime
from celery import Celery
import logging
import pymysql
import pymongo

app = Celery(
    'myapp',
    broker='redis://192.168.0.175:6379/0',
)

key_words = ['id', 'area', 'city', 'corporate_name', 'name', 'category_name', 'product_name',
             'subscription_date', 'quantity', 'unit_price', 'sum_money', 'year', 'month', 'week', 'timestamp']

def get_sql_conn():
    conn = pymysql.Connection(host='192.168.0.186', port=3306, user='root', password='Nash1234@',
                              charset='utf8', db='test')
    return conn

def get_mongo_doc():
    conn = pymongo.MongoClient('192.168.0.186', port=20000)
    doc = conn.test.data
    return doc

@app.task
def add(sql):
    conn = get_sql_conn()
    doc = get_mongo_doc()
    with conn.cursor() as cursor:
        cursor.execute(sql)
        tmp = []
        for i in cursor.fetchall():
            tmp.append(dict(zip(key_words, i)))
        if tmp:
            doc.insert_many(tmp, bypass_document_validation=True)
    conn.close()

@app.task
def ddd():

    page_num = 500
    conn = get_sql_conn()
    with conn.cursor() as cursor:
        cursor.execute('select max(id), min(id), COUNT(*) from test_update;')
        num = cursor.fetchall()[0]
        logging.warn(num)
        logging.warn(num[0]-num[1])
        if num:
            for i in xrange(num[1], num[0]+1, page_num):
                sql = 'select * from test_update where id>={} and id<{};'.format(i, i+page_num)
                add.delay(sql)

if __name__ == '__main__':
    app.start()
#coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: monitor.py
@datetime: 3/14/2019 1:55 PM
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


import pymongo
import datetime
import time


conn = pymongo.MongoClient('192.168.0.186', port=20000)
doc = conn.test.data

tmp = 0
while True:

    count = doc.count()
    if count != tmp:
        print datetime.datetime.now(), count, (count-tmp)/5
        tmp = count
    time.sleep(5)
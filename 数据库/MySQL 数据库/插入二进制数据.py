#coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: 插入二进制数据.py
@datetime: 2019-2-19 11:14
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')



import pymysql

with open('0.gif', 'rb') as f:
    img = f.read()


db = pymysql.connect("192.168.0.186","root","Nash1234@","allen")
cursor = db.cursor()

#cursor.execute("INSERT INTO demo_pic_repo SET touxiang_data= %s" % pymysql.Binary(img))

sql = "insert into tutorials_tbl (y) VALUE (%s)"
cursor.execute(sql, img)


db.commit()
cursor.close()
db.close()


# results = cursor.fetchall()
#
# for row in results:
#     for i in row:
#         print i,
#
# db.close()
# coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: red.py
@datetime: 2018-4-2 14:00
"""

from __future__ import unicode_literals

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import xlrd

workbook = xlrd.open_workbook(u'aaa.xlsx')

# sheet_names = workbook.sheet_names()

sheet = workbook.sheet_by_index(0)

tmp = set()
for i in xrange(1, sheet.nrows):
    rows = sheet.row_values(i)

    if rows[5] not in tmp:
        tmp.add(rows[5])
        print '(','\'',rows[4].strip(), '\'' ,  ','  , '\'' ,  rows[5].strip(), '\''  ,  ',',  rows[8],  ')'  ,  ','

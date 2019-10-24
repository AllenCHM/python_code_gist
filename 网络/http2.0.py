#coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: http2.0.py
@datetime: 2019-2-20 16:39
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# pip install hyper

from hyper import HTTPConnection

conn = HTTPConnection('http2bin.org:443')
conn.request('GET', '/get')
resp = conn.get_response()

print(resp.read())
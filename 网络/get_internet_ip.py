#coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: get_internet_ip.py
@datetime: 3/14/2019 3:49 PM
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import re


url = urllib2.urlopen("http://txt.go.sohu.com/ip/soip")
text = url.read()
key1 = 'user_ip'
key2 = ';'
# s = text.find(key1)
# e = text.find(key2,s)
# IP = text[s:e]
# print IP

ip = re.findall(r'\d+.\d+.\d+.\d+', text)
print ip[0]

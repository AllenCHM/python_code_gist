#coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: http请求.py
@datetime: 2019-2-20 16:37
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# pip install requests

import requests


# GET方法
r = requests.get('https://api.github.com/events')

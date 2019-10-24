#coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: test.py
@datetime: 3/19/2019 3:15 PM
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


from PIL import Image

def getImage():
    fileName = '16.jpg'
    img = Image.open()
    # 打印当前图片的模式以及格式
    print('未转化前的: ', img.mode, img.format)
    # 使用系统默认工具打开图片
    # img.show()
    return img
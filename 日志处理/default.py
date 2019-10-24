#coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: default.py
@datetime: 3/11/2019 11:44 AM
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')



import logging

def get_logger():
    #     """
    #         设置全局logging 输出，并兼容docker日志输出
    #     :param level:
    #     :return:
    #     """
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

logger = get_logger()
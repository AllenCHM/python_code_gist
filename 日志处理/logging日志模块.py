# coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: logging日志模块.py
@datetime: 2019-2-20 17:07
"""

from __future__ import unicode_literals

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import logging
import os
import time

THISFILEPATH = os.path.dirname(os.path.realpath(__file__))
logfile = '{path}/python_test_file.log'.format(path=THISFILEPATH)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s - [line:%(lineno)d] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    filename=logfile,
                    # level=10,
                    filemode='a')

logging.info("This is a info.\n")
logging.warn("This is a warning.\n")
logging.error("This is a error.\n")
# logging.log("This is a log. \n\n")
logging.debug("This is a debug. \n\n")
logging.critical("This is a critical \n\n\n")

logging.info("now time is {time}".format(time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
logging.info("normal type , today is {today} , yesterday is {yesterday} , tomorrow is {tommorrow} .".format(today=today,
                                                                                                            yesterday=yesterday,
                                                                                                            tommorrow=tomorrow))
logging.info(
    "nyr style , today is {today} , yesterday is {yesterday} , tommrrow is {tommorrow} .".format(today=Today_nyr,
                                                                                                 yesterday=Yesterday_nyr,
                                                                                                 tommorrow=Tomorrow_nyr))

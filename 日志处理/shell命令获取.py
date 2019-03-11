# coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: shell命令获取.py
@datetime: 2019-2-20 17:08
"""

from __future__ import unicode_literals

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import logging
import subprocess

shell_cmd = "df -h | awk '{print $1}'"
p = subprocess.Popen("{cmd}".format(cmd=shell_cmd), shell=True, stdout=subprocess.PIPE)
out = p.stdout.readlines()
for line in out:
    print line.strip()
    logging.info(" file system is :{line}  .".format(line=line.strip()))

# 获取命令方法二：
for line in subprocess.Popen("df -h | awk '{print $1}'", shell=True, stdout=subprocess.PIPE).stdout.readlines():
    print line.strip()
    logging.info(" file system is :{line}  .".format(line=line.strip()))

#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import os
from logging import log

def run(cmd_str, fatal=True):
    # this is not a good implement
    log.command(log.term.cmd(cmd_str))
    ret = os.system(cmd_str)
    if ret is not 0:
        if fatal:
            log.error('[ERROR] run cmd: %s failed', cmd_str)
            os._exit(1)
        else:
            log.info('[INFO] %s is not fatal' % cmd_str)
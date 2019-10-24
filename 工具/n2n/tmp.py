#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


import socket
import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)

while True:
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(3)
    try:
        sk.connect(('10.0.0.248', 27017))
    except Exception:
        logger.warning(' \033[1;31;mServer port 27017 is close\033[0m')
    sk.close()
    time.sleep(1)
#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


tag='hx/mitaka_compute/12.0.0'
[m.start() for m in re.finditer('/',tag)]
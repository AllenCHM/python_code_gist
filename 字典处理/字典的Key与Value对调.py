# coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

m = {'A': 1, 'B': 2, 'C': 3}
invert_map_key_value = lambda m: dict(zip(m.values(), m.keys()))
invert_map_key_value(m)

# coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from collections import Counter

A = Counter({'a': 1, 'b': 2, 'c': 3})
B = Counter({'b': 3, 'c': 4, 'd': 5})
A + B

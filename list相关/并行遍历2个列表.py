#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


a = [1, 2, 3]
b = [4, 5, 6]

for (a_val, b_val) in zip(a, b):
    print(a_val, b_val)
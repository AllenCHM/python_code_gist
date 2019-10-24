# coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

a = {'name': 'michael', 'age': "27", 'sex': 'male'}
b = {'name': 'hqh', 'age': '27'}
{k: a[k] for k in a.keys() - b.keys()}
dict(a.items() - b.items())

# 需要注意的是，当字典的值有字典时，a.items()-b.items() 这种方式会报错 TypeError: unhashable type: 'dict'；

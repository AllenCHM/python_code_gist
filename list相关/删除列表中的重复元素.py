#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 下面这种方法不能维持顺序
x = [1, 8, 4, 5, 5, 5, 8, 1, 8]
list(set(x))


# 可以维持顺序
from collections import OrderedDict
x = [1, 8, 4, 5, 5, 5, 8, 1, 8]
list(OrderedDict.fromkeys(x))
# coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 输入的两个数组，输出一个是数组&值相加或者相乘

first = [1, 2, 3, 4, 5]
second = [6, 7, 8, 9, 10]

# output
three = [7, 9, 11, 13, 15]

# The zip function is useful here, used with a list comprehension.
# add
[x + y for x, y in zip(first, second)]

# other
[x * y for x, y in zip(first, second)]
[max(x, y) for x, y in zip(first, second)]

# coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from itertools import islice

ls = [1, 2, 3, 5, 8]
diff = [j - i for i, j in zip(ls, islice(ls, 1, None))]
print(diff)

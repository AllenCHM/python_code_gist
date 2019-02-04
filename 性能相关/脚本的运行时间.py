#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import time

start_time = time.clock()

for i in range(10000000):
    pass

elapsed_time = time.clock() - start_time
print("Time elapsed: {} seconds".format(elapsed_time))

# Out
# Time elapsed: 0.30121700000000007 seconds


import timeit
elapsed_time = timeit.timeit('for i in range(10000000): pass', number=1)
print("Time elapsed: {} seconds".format(elapsed_time))

# Out
# Time elapsed: 0.2051873060000844 seconds
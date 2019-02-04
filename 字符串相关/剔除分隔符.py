#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


''.join('A|B|C|D|E|F|G'.split('|'))

# 用 itertools.islice，因为可以节选字符串：
import itertools

''.join(itertools.islice('A|B|C|D|E|F|G', 6, None, 2))
# output: 'DEFG'

''.join(itertools.islice('A|B|C|D|E|F|G', 0, None, 2))
# output: ''ABCDEFG'
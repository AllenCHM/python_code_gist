#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


import pprint as pp
animals = [{'animal': 'dog', 'legs': 4, 'breeds': ['Border Collie', 'Pit Bull', 'Huskie']}, {'animal': 'cat', 'legs': 4, 'breeds': ['Siamese', 'Persian', 'Sphynx']}]
pp.pprint(animals, width=1)

# # Out
# [{'animal': 'dog',
#   'breeds': ['Border '
#              'Collie',
#              'Pit '
#              'Bull',
#              'Huskie'],
#   'legs': 4},
#  {'animal': 'cat',
#   'breeds': ['Siamese',
#              'Persian',
#              'Sphynx'],
#   'legs': 4}]

# width参数指定一行上最大的字符数。设置width为1确保字典打印在单独的行
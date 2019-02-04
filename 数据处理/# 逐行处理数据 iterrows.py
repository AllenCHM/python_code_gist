#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 逐行处理数据 iterrows

for idx, row in data.iterrows():
    project_name=row['projectName']
    tag_name=row['tagName']
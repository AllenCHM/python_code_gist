#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# ipython中直接打印df，中文没有乱码，但是to_csv方法存储时，中文有乱码。
df.to_csv('file.csv',encoding='utf-8-sig')

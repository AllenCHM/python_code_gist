#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


[ name for name in os.listdir(thedir) if os.path.isdir(os.path.join(thedir, name)) ]

filter(os.path.isdir, os.listdir(os.getcwd()))
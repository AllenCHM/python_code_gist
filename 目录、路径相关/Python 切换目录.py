#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import os
import contextlib


# 执行完，返回之前目录


path = '.'

@contextlib.contextmanager
def cdir(path):
    prev_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)


def func():
    os.chdir('..')
    print os.getcwd()

print os.getcwd()
with cdir(path):
    func()
print os.getcwd()

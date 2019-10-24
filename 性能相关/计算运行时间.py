# coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import time


class Timer(object):
    def __enter__(self):
        self.error = None
        self.start = time.time()
        return self

    def __exit__(self, type, value, tb):
        self.finish = time.time()
        if type:
            self.error = (type, value, tb)

    def duration(self):
        return self.finish - self.start


def func():
    pass


with Timer() as timer:
    func()
timer.duration()

# Out
# 0.29994797706604004

#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# strptime 是将字符串转换为 datetime，
# 其实这个方法的全称是 “string parse time”，叫做字符串解析成时间，重点在解析（parse）:

from datetime import datetime

date_obj = datetime.strptime('2018-10-15 20:59:29', '%Y-%m-%d %H:%M:%S')
print(type(date_obj),date_obj)

# Out
# <class 'datetime.datetime'> 2018-10-15 20:59:29


# strftime 是将 datetime 转换为字符串，全称是 “string format time”，
# 翻译过来就是将字符串的形式来格式化时间，重点在格式化（format），使之以一种可读的字符串形式返回：
from datetime import datetime
date_obj = datetime.now()
date_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(type(date_string),date_string)

# Out
# <class 'str'> 2019-01-05 18:41:04
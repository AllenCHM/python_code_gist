#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import re
# 文件名字中含有特殊字符转成空格，因为？‘’等作为文件名是非法的。以下正则表达式进行过滤转换

name = 'asdfasd sdfasd的说法——)((*&**……*……'
newname = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]",' ', name)
print newname

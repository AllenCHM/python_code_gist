#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


import subprocess

subprocess.call(['mkdir', 'empty_folder'])

# 运行一条命令并输出得到的结果
output = subprocess.check_output(['ls', '-l'])

# 上面的调用是阻塞的
# 如果运行shell中内置的命令，如cd或者dir，需要指定标记shell=True
output = subprocess.call(['cd', '/'], shell=True)

# 对于更高级的用例，可以使用 Popen constructor。

# Python 3.5引进了一个新的run函数，它的行为与call和check_output很相似。如果你使用的是3.5版本或更高版本，
# 看一看run的文档，里面有一些有用的例子。否则，如果你使用的是Python 3.5以前的版本或者你想保持向后兼容性，
# 上面的call和check_output代码片段是你最安全和最简单的选择
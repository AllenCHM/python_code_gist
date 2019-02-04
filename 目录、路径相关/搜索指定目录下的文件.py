#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 将指定目录及其子目录下的文件搜索出来：
def find_file(start_path, name):
    """
    search the files of name from the dir start_path，存放的是搜索文件的路径
    :param start_path: the search scope of dir
    :param name: the name of search file
    :return: set of files path
    """
    files_path = set()
    for rel_path, dirs, files in os.walk(start_path):
        # if name in files:
        for f in files:
            if name in f:
                full_path = os.path.join(start_path, rel_path, f)
                path = os.path.normpath(os.path.abspath(full_path))
                files_path.add(path)
    return files_path
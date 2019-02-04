#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
# 可以计算文件的 md5、sha256 等值

# https://pymotw.com/3/hashlib/index.html#module-hashlib
def get_verify_value(file_path, verify_type):
    """
    计算指定文件的校验值
    :param file_path: 文件路径
    :param verify_type: 校验值类型，md5 sha256 等等
    :return:
    """
    h = hashlib.new(verify_type)
    if not file_path:
        return None
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(4096), b""):
            h.update(block)
    return h.hexdigest()
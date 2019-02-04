#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def download_package(self, package_url):
    print("start download_build_result")
    if not package_url.endswith("/"):
        package_url += '/'
    cmd = "wget -c -r -nd -np -P %s %s" % ("output", package_url)
    print(cmd)
    os.system(cmd)
    print(os.getcwd())
    print("finish download_build_result")
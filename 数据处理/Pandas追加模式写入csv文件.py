# coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import pandas as pd

data = pd.DataFrame([[1, 2, 3]])
csv_headers = ['A', 'B', 'C']
data.to_csv('./Marvel3_yingpping.csv', header=csv_headers, index=False, mode='a+', encoding='utf-8')
data = pd.DataFrame([[4, 5, 6]])
data.to_csv('./Marvel3_yingpping.csv', header=False, index=False, mode='a+', encoding='utf-8')
data = pd.DataFrame([[7, 8, 9]])
data.to_csv('./Marvel3_yingpping.csv', header=False, index=False, mode='a+', encoding='utf-8')

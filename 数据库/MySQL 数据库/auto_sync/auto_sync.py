# coding=utf-8
"""
@author: AllenCHM
@contact: chengchuanming@itssoft.net
@file: auto_sync.py.py
@datetime: 2018-4-2 11:28
"""

from __future__ import unicode_literals

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import random
import datetime
import time
import logging

def get_logger():
    #     """
    #         设置全局logging 输出，并兼容docker日志输出
    #     :param level:
    #     :return:
    #     """
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)
    return logger

logger = get_logger()

import pymysql
conn = pymysql.Connection(host='192.168.0.186', port=3306, user='root', password='Nash1234@',
                          charset='utf8', db='test')
cursor = conn.cursor()

# cursor.execute('show databases')
# a = cursor.fetchall()

area = [
    "西北",
    "华南",
    "华北",
    "华东",
    "西南",
    "东北"
]

city = [
    "南昌",
    "青岛",
    "上海",
    "西安",
    "秦皇岛",
    "深圳",
    "张家口",
    "南京",
    "温州",
    "天津",
    "石家庄",
    "厦门",
    "北京",
    "常州",
    "成都",
    "大连",
    "海口",
    "重庆"
]

name = [
    "丫头",
    "banber测试",
    "协作3",
    "xing……",
    "〞奶、茶.",
    "南鸢终念",
    "陈理WX",
    "Jean","Allen_小铭试也","Allen","Allen-大数据","吕骏-Big Data","不忘初心","仰望星空",
    "清欢",
    "programmer",
    "Six",
    "、FenG",
    "FenG",
    "VIP",
    "撒哈拉牧马人",
    "等一阵峰",
    "Cenizas",
    "7℃ sun shine"
]

compeny = [
    "春永建设",
    "五金机械",
    "文成",
    "同恒",
    "国银贸易",
    "仲堂企业",
    "世邦",
    "东南实业",
    "亚太公司",
    "迈多贸易",
    "悦海",
    "森通",
    "伸格公司",
    "山泰企业",
    "瑞栈工艺",
    "赐芳股份",
    "百达电子",
    "昇昕股份有限公司",
    "富泰人寿",
    "光明杂志",
    "威航货运有限公司",
    "祥通",
    "上河工业",
    "建国科技",
    "东旗",
    "永业房屋",
    "嘉业",
    "顶上系统",
    "中硕贸易",
    "东帝望",
    "康浦",
    "通恒机械",
    "师大贸易",
    "迈策船舶",
    "兰格英语",
    "学仁贸易",
    "华科",
    "和福建设",
    "升格企业",
    "汉光企管",
    "红阳事业",
    "凯旋科技",
    "大钰贸易",
    "实翼",
    "协昌妮绒有限公司",
    "正太实业",
    "千固",
    "富同企业",
    "坦森行贸易",
    "就业广兑"
]

product = [
    ('饮料', '苹果汁', 11.5),
    ('饮料', '牛奶', 13.8),
    ('饮料', '汽水', 3.3),
    ('饮料', '啤酒', 10.6),
    ('饮料', '蜜桃汁', 13.2),
    ('饮料', '绿茶', 202.4),
    ('饮料', '运动饮料', 14.3),
    ('饮料', '柳橙汁', 31.6),
    ('饮料', '矿泉水', 10.6),
    ('饮料', '苏打水', 10.1),
    ('饮料', '浓缩咖啡', 5.0),
    ('饮料', '柠檬汁', 14.0),
    ('调味品', '蕃茄酱', 7.8),
    ('调味品', '盐', 17.1),
    ('调味品', '麻油', 16.8),
    ('调味品', '酱油', 16.2),
    ('调味品', '胡椒粉', 25.6),
    ('调味品', '味精', 12.0),
    ('调味品', '蚝油', 14.4),
    ('调味品', '海鲜酱', 18.2),
    ('调味品', '甜辣酱', 34.0),
    ('调味品', '海苔酱', 14.4),
    ('调味品', '肉松', 12.6),
    ('调味品', '辣椒粉', 10.0),
    ('点心', '饼干', 12.6),
    ('点心', '糖果', 6.6),
    ('点心', '桂花糕', 58.3),
    ('点心', '花生', 7.6),
    ('点心', '巧克力', 10.5),
    ('点心', '棉花糖', 24.4),
    ('点心', '牛肉干', 31.6),
    ('点心', '蛋糕', 6.2),
    ('点心', '玉米片', 9.3),
    ('点心', '薯条', 13.9),
    ('点心', '玉米饼', 11.2),
    ('点心', '山渣片', 32.7),
    ('点心', '绿豆糕', 9.2),
    ('日用品', '大众奶酪', 15.8),
    ('日用品', '德国奶酪', 25.8),
    ('日用品', '温馨奶酪', 9.2),
    ('日用品', '白奶酪', 21.5),
    ('日用品', '浪花奶酪', 1.8),
    ('日用品', '光明奶酪', 41.4),
    ('日用品', '花奶酪', 24.5),
    ('日用品', '黑奶酪', 25.1),
    ('日用品', '意大利奶酪', 14.1),
    ('日用品', '酸奶酪', 28.5),
    ('谷类/麦片', '糯米', 15.8),
    ('谷类/麦片', '燕麦', 6.2),
    ('谷类/麦片', '糙米', 8.0),
    ('谷类/麦片', '三合一麦片', 5.3),
    ('谷类/麦片', '白米', 28.0),
    ('谷类/麦片', '小米', 14.4),
    ('谷类/麦片', '黄豆', 22.1),
    ('肉/家禽', '鸡', 62.9),
    ('肉/家禽', '猪肉', 11.3),
    ('肉/家禽', '鸭肉', 85.1),
    ('肉/家禽', '盐水鸭', 22.8),
    ('肉/家禽', '鸡肉', 5.6),
    ('特制品', '海鲜粉', 22.3),
    ('特制品', '沙茶', 16.6),
    ('特制品', '烤肉酱', 30.2),
    ('特制品', '猪肉干', 34.3),
    ('特制品', '鸡精', 7.3),
    ('海鲜', '蟹', 24.3),
    ('海鲜', '龙虾', 3.9),
    ('海鲜', '墨鱼', 42.5),
    ('海鲜', '黄鱼', 19.3),
    ('海鲜', '鱿鱼', 12.8),
    ('海鲜', '干贝', 16.8),
    ('海鲜', '虾米', 12.9),
    ('海鲜', '虾子', 7.2),
    ('海鲜', '雪鱼', 7.1),
    ('海鲜', '蚵', 9.5),
    ('海鲜', '海参', 9.6),
    ('海鲜', '海哲皮', 11.2)
]

weeks = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']


def generate_data():
    '''
         生成一条数据
     :return:
    '''
    r_area = random.choice(area)
    r_city = random.choice(city)
    r_compeny = random.choice(compeny)
    r_name = random.choice(name)
    r_product_info = random.choice(product)
    r_product_tag = r_product_info[0]
    r_product_name = r_product_info[1]
    r_date = datetime.datetime.now().date() - datetime.timedelta(days=(random.randint(1, 1000)))
    r_product_num = random.randint(10,100)
    r_product_price = r_product_info[2]
    r_product_sum_money = r_product_price * r_product_num
    r_year = r_date.day
    r_month = r_date.month
    r_week = weeks[r_date.weekday()]
    r_timestamp = datetime.datetime.now()
    return (r_area, r_city, r_compeny, r_name, r_product_tag, r_product_name, r_date, r_product_num, r_product_price, \
            r_product_sum_money, r_year, r_month, r_week, r_timestamp)

def generate_data_by_name(name):
    '''
         按照name生成一条数据
     :return:
    '''
    r_area = random.choice(area)
    r_city = random.choice(city)
    r_compeny = random.choice(compeny)
    r_name = name
    r_product_info = random.choice(product)
    r_product_tag = r_product_info[0]
    r_product_name = r_product_info[1]
    r_date = datetime.datetime.now().date() - datetime.timedelta(days=(random.randint(1, 1000)))
    r_product_num = random.randint(10,100)
    r_product_price = r_product_info[2]
    r_product_sum_money = r_product_price * r_product_num
    r_year = r_date.day
    r_month = r_date.month
    r_week = weeks[r_date.weekday()]
    r_timestamp = datetime.datetime.now()
    return (r_area, r_city, r_compeny, r_name, r_product_tag, r_product_name, r_date, r_product_num, r_product_price, \
            r_product_sum_money, r_year, r_month, r_week, r_timestamp)



def insert_data(data):
    '''
         插入多条数据
                 [(地区, 城市, 公司名称, 姓名, 类别名称, 产品名称, 订购日期, 数量, 单价, 金额, 年, 月份, 星期, 时间戳), ]

     :param data:
     :return:
    '''
    sql = 'INSERT INTO test_update (`地区`, `城市`, `公司名称`, `姓名`, `类别名称`, `产品名称`, ' \
          '`订购日期`, `数量`, `单价`, `金额`, `年`, `月份`, `星期`, `时间戳`) VALUES (' \
          '\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(*data)
    logger.debug(sql)
    cursor.execute(sql)

def commit_data():
    '''
        提交数据
    '''
    conn.commit()


def init_db(rows_num):
    '''
        初始化数据库
    :param rows_num:  数据行数， int
    :return:
    '''
    for i in xrange(rows_num):
        data = generate_data()
        insert_data(data=data)
    conn.commit()

def get_db_rows_num():
    '''
        获取数据总行数
    :return:  数据总行数，int
    '''
    cursor.execute('select count(*) from test_update')
    num = cursor.fetchone()
    return num[0]

def get_db_old_data_ids(old_data_rows_num):
    '''
        获取老数据的id
    :param old_data_rows_num: 老数据行数
    :return:
    '''
    cursor.execute('select id FROM test_update order by `时间戳` ASC limit 0,{}'.format(old_data_rows_num))
    ids = [i[0] for i in cursor.fetchall()]
    return ids

def delete_data_by_ids(ids):
    '''
        删除老数据
    :param ids:
    :return:
    '''
    for id in ids:
        sql = 'delete from test_update WHERE id={}'.format(id)
        cursor.execute(sql)
    commit_data()

def get_old_data_rows(save_rows):
    '''
        获取数据总行数
    :param save_rows:
    :return:
    '''
    total_rows = get_db_rows_num()
    logger.info(total_rows-save_rows)

def check_name_in_db():
    for i in name:
        sql = 'select count(*) from test_update where 姓名=\'{}\''.format(i)
        cursor.execute(sql)
        num = cursor.fetchone()
        if num[0]>0:
            data = generate_data_by_name(i)
            insert_data(data=data)
    commit_data()

if __name__ == '__main__':
    #插入一行数据
    MAX_COUNT = 2000000
    logger.info('插入一行数据')
    data = generate_data()
    insert_data(data=data)
    commit_data()
    #检查数据库总行数
    num = get_db_rows_num()

    logger.info(num)
    #删除多余行数据（最大100行）
    if num > MAX_COUNT:
        logger.debug('删除多余数据')
        ids = get_db_old_data_ids(num-MAX_COUNT)
        delete_data_by_ids(ids)
    elif num < MAX_COUNT:
        logger.warn('数据不足，增加数据')
        for _ in xrange((MAX_COUNT-num+9)/10):
            for i in xrange(10):
                data = generate_data()
                insert_data(data=data)
            commit_data()
    # check_name_in_db()
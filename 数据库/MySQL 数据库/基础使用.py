#coding=utf-8
__author__ = 'AllenCHM'
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


db = MySQLdb.connect("localhost","your_username","your_password","your_dbname")
cursor = db.cursor()
sql = "select Column1,Column2 from Table1"
cursor.execute(sql)
results = cursor.fetchall()

for row in results:
    print row[0]+row[1]

db.close()
import datetime
import time

# print time HOURS:MINUTES:SECONDS
# e.g., '10:50:58'
print(time.strftime("%H:%M:%S"))

# print current date DAY:MONTH:YEAR
# e.g., '05/01/2019'
print(time.strftime("%d/%m/%Y"))

# Out
# 15:18:03
# 05/01/2019


today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days=1)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
Today_nyr = int(datetime.datetime.strftime(today, '%Y%m%d'))
Yesterday_nyr = int(datetime.datetime.strftime(yesterday, '%Y%m%d'))
Tomorrow_nyr = int(datetime.datetime.strftime(tomorrow, '%Y%m%d'))
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

print "now time is {time}".format(time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print "normal type , today is {today} , yesterday is {yesterday} , tomorrow is {tommorrow} .".format(today=today,
                                                                                                     yesterday=yesterday,
                                                                                                     tommorrow=tomorrow)
print "nyr style , today is {today} , yesterday is {yesterday} , tommrrow is {tommorrow} .".format(today=Today_nyr,
                                                                                                   yesterday=Yesterday_nyr,
                                                                                                   tommorrow=Tomorrow_nyr)

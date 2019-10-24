mysql数据连接器通过pymysql连接到远程的MySQL数据库，并根据配置的信息生成查询
SQL语句并发送到远程MySQL数据库，并将该SQL语句执行返回结果，
然后使用数据同步自定义的数据类型拼装为抽象的数据集，并传递给下游数据处理。


简而言之，通过pymysql连接远程mysql数据库，并执行相应的SQL语句，将数据从MySQL中Select出来，从
底层实现了从MySQL数据库中读取数据。

mysql数据连接器支持读取表和视图。表字段可以依序指定全部列、指定部分列、调整列顺序、
指定常量字段和配置MySQL的函数如now() 等。



类型分类| MySQL数据类型
---|---
整数类| int，tinyint，smallint，mediumint，bigint
浮点类|float，double，decimal
字符串类|varchar，char，tinytext，text，mediumtext，longtext
日期时间类|date，datetime，timestamp，time，year
布尔类|bit，bool
二进制类|tinyblob，mediumblob，blob，longblob，varbinary


注意：

· 除上述罗列字段类型外，其他类型均不支持。例如：BINARY、
    VARBINARY、ENUM、SET、Geometry、Point、MultiPoint、
    LineString、MultiLineString、Polygon、GeometryCollection

· 将tinyint(1)视作整型

· [PyMySQL](https://pymysql.readthedocs.io/en/latest/user/resources.html)版本0.7.11。需要确认返回数据是否与上一致







# mysql数据类型详解(知识补充)

## 整型

MySQL数据类型| 含义| pymysql数据类型
---|---|---
int| 4个字节  范围(-2147483648~2147483647) | int
tinyint|1个字节  范围(-128~127)| int
smallint|2个字节  范围(-32768~32767)| int
mediumint|3个字节  范围(-8388608~8388607)| int
bigint|8个字节  范围(+-9.22*10的18次方)| int

取值范围如果加了unsigned，则最大值翻倍。如tinyint unsigned的取值范围为(0~256)。

## 浮点类

MySQL数据类型| 含义| pymysql数据类型
---|---|---
float| 单精度浮点型    8位精度(4字节)     m总个数，d小数位 | float
double|双精度浮点型    16位精度(8字节)    m总个数，d小数位 | float
decimal|2个字节  范围(-32768~32767) | Decimal

设一个字段定义为float(6,3)，如果插入一个数123.45678,实际数据库里存的是123.457，
但总个数还以实际为准，即6位。整数部分最大是3位，如果插入数12.123456，
存储的是12.1234，如果插入12.12，存储的是12.1200.

decimal(m,d) 参数m<65 是总个数，d<30且 d<m 是小数位。

## 字符串

MySQL数据类型| 含义| pymysql数据类型
---|---|---
varchar| 固定长度，最多65535个字符 | str
char|固定长度，最多255个字符 | str
tinytext|可变长度，最多255个字符 | str
text|可变长度，最多65535个字符 | str
mediumtext|可变长度，最多2的24次方-1个字符 | str
longtext|可变长度，最多2的32次方-1个字符 | str


## 日期时间类

MySQL数据类型| 含义| pymysql数据类型
---|---|---
date| YYYY-MM-DD的格式显示，比如：2009-07-19 | date
datetime|以YYYY-MM-DD HH:MM:SS的格式显示，比如：2009-07-19 11：22：30 | datetime
timestamp|以YYYY-MM-DD的格式显示，比如：2009-07-19 | datetime
time|以HH:MM:SS的格式显示。比如：11：22：30 | timedelta
year|以YYYY的格式显示。比如：2009 | int

若定义一个字段为timestamp，这个字段里的时间数据会随其他字段修改的时候自动刷新，
所以这个数据类型的字段可以存放这条记录最后被修改的时间。


## 布尔类

MySQL数据类型| 含义| pymysql数据类型
---|---|---
bit| 无符号[0,255]，有符号[-128,127],BIT和BOOL布尔型都占用1字节 | str
bool|占用1字节 | int

## 二进制类

MySQL数据类型| 含义| pymysql数据类型
---|---|---
tinyblob| Max:255， |str
mediumblob|Max:16M，|str
blob|Max:64K ， |str
longblob|Max:4G|str
varbinary|类似VarChar的变长二进制存储，特点是定长不补0|str

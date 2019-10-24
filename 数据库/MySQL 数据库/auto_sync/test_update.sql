CREATE TABLE IF NOT EXISTS `test_update`(
   `id` INT PRIMARY KEY AUTO_INCREMENT,
   `area` VARCHAR(100) NOT NULL COMMENT '地区',
   `city` VARCHAR(100) NOT NULL COMMENT '城市',
   `corporate_name` VARCHAR(100) NOT NULL COMMENT '公司名称',
   `name` VARCHAR(100) NOT NULL COMMENT '姓名',
   `category_name` VARCHAR(100) NOT NULL COMMENT '类别名称',
   `product_name` VARCHAR(100) NOT NULL COMMENT '产品名称',
   `subscription_date` VARCHAR(100) NOT NULL COMMENT '订购日期',
   `quantity` INT NOT NULL COMMENT '数量',
   `unit_price` FLOAT NOT NULL COMMENT '单价',
   `sum_money` FLOAT NOT NULL COMMENT '金额',
   `year` INT NOT NULL COMMENT '年',
   `month` INT NOT NULL COMMENT '月份',
   `week` VARCHAR(100) NOT NULL COMMENT '星期',
   `timestamp` TIMESTAMP NOT NULL COMMENT '时间戳'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `test_update`(
   `id` INT PRIMARY KEY AUTO_INCREMENT,
   `地区` VARCHAR(100) NOT NULL COMMENT '地区',
   `城市` VARCHAR(100) NOT NULL COMMENT '城市',
   `公司名称` VARCHAR(100) NOT NULL COMMENT '公司名称',
   `姓名` VARCHAR(100) NOT NULL COMMENT '姓名',
   `类别名称` VARCHAR(100) NOT NULL COMMENT '类别名称',
   `产品名称` VARCHAR(100) NOT NULL COMMENT '产品名称',
   `订购日期` VARCHAR(100) NOT NULL COMMENT '订购日期',
   `数量` INT NOT NULL COMMENT '数量',
   `单价` FLOAT NOT NULL COMMENT '单价',
   `金额` FLOAT NOT NULL COMMENT '金额',
   `年` INT NOT NULL COMMENT '年',
   `月份` INT NOT NULL COMMENT '月份',
   `星期` VARCHAR(100) NOT NULL COMMENT '星期',
   `时间戳` TIMESTAMP NOT NULL COMMENT '时间戳'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
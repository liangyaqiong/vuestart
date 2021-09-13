import pymysql

# 告诉 Django 使用 pymysql 模块连接 mysql 数据库
# .ImproperlyConfigured: mysqlclient 1.4.0 or newer is required; you have 0.10.1

pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库
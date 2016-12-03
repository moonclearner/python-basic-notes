# coding:utf8

import MySQLdb

# print MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='test',
    charset='utf8'
)

#数据库连接

cursor = conn.cursor()

sql_insert = "insert into testpy(ID,Name) values(4274,'Name5') "
sql_update = "update testpy set Name='yyyy' where ID=1"
sql_delete = "delete from testpy where ID = 3"


#抛出异常

try:
    cursor.execute(sql_insert)
    print cursor.rowcount
    cursor.execute(sql_update)
    print cursor.rowcount
    cursor.execute(sql_delete)
    print cursor.rowcount
    conn.commit()
except Exception as e:
    print e
    conn.rollback()


cursor.close()

conn.close()

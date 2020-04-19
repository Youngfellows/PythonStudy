# coding=utf-8
import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.249.143",
    user="root",
    passwd="3282",
    database="python4"
)

if __name__ == "__main__":
    print(mydb)
    # 1. 创建数据库
    mycorsor = mydb.cursor()
    # mycorsor.execute("create database python4")

    # 2. 创建表
    mycorsor.execute("use python4")
    # mycorsor.execute("create table person(name varchar(40),age int)")
    mycorsor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")
    # mycorsor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

    # 3. 输出所有数据库列表
    print("=================== 3. 输出所有数据库列表 ===================")
    mycorsor.execute("SHOW DATABASES")
    for database in mycorsor:
        print(database)

    # 4. 查看数据表是否已存在
    print("=================== 4. 查看数据表是否已存在 ===================")
    mycorsor.execute("SHOW TABLES")
    for table in mycorsor:
        print("tpye(table) = {} table = {}".format(type(table), table))

    # 5. 主键设置
    # mycorsor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

    # 6. 插入数据
    sql = "INSERT INTO sites (name,url) VALUES (%s,%s)"
    values = ("baidu", "www.baidu.com")
    mycorsor.execute(sql, values)
    mydb.commit()  # 提交事务
    insert_id = mycorsor.lastrowid
    print("insert into data success")
    print("1条数据插入成功,ID:{}".format(insert_id))

    # 7. 批量插入
    sql = "INSERT INTO sites (name,url) VALUES (%s,%s)"
    values = [("Google", "www.google.com"),
              ("github", "www.github.com"),
              ("Tencent", "www.qq.com"),
              ("Apple", "www.apple.com")]
    mycorsor.executemany(sql, values)
    mydb.commit()
    count = mycorsor.rowcount
    print("插入{}数据成功...".format(count))

    # 8. 查询数据
    print("=================== 8. 查询数据 ===================")
    mycorsor.execute("SELECT * FROM sites")
    # 获取所有记录
    qyery_all = mycorsor.fetchall()
    for row in qyery_all:
        print(row)

    print("=================== 9. 也可以读取指定的字段数据 ===================")
    mycorsor.execute("SELECT name, url FROM sites")
    query_all = mycorsor.fetchall()
    for row in query_all:
        print(row)

    print("=================== 10. 如果我们只想读取一条数据，可以使用 fetchone()  ===================")
    # mycorsor.execute("SELECT name,url FROM sites")
    # row = mycorsor.fetchone()
    # print(row)

    print("=================== 11. where 条件语句  ===================")
    mycorsor.execute("SELECT * FROM sites WHERE name='Google'")
    query_all = mycorsor.fetchall()
    for row in query_all:
        print(row)

    print("=================== 12. where 条件语句 ,也可以使用通配符 % ===================")
    sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"
    mycorsor.execute(sql)
    query_all = mycorsor.fetchall()
    for row in query_all:
        print(row)

    print("=================== 12. 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件： ===================")
    sql = "SELECT * FROM sites WHERE name = %s"
    quer_name = ("Apple",)
    mycorsor.execute(sql, quer_name)
    query_all = mycorsor.fetchall()
    for row in query_all:
        print(row)

    print("=================== 13.排序 ===================")
    sql = "SELECT * FROM sites ORDER BY name "
    mycorsor.execute(sql)
    query_all = mycorsor.fetchall()
    for row in query_all:
        print(row)

    print("=================== 13.按 name 字段字母的降序排序 ===================")
    sql = "SELECT * FROM sites ORDER BY name DESC"
    mycorsor.execute(sql)
    query_all = mycorsor.fetchall()
    for row in query_all:
        print(row)

    print("=================== 14.如果我们要设置查询的数据量，可以通过 LIMIT 语句来指定 ===================")
    # sql = "SELECT * FROM sites LIMIT 3"
    sql = "SELECT * FROM sites ORDER  BY RAND() LIMIT 5"
    mycorsor.execute(sql)
    query_all = mycorsor.fetchall()
    for row in query_all:
        print(row)

    # 随机查询
    print("=================== 14.随机查询1条 ===================")
    # sql = "SELECT * FROM sites WHERE id >= (SELECT FLOOR( MAX(id) * RAND()) FROM sites )ORDER BY id LIMIT 1;"
    sql = "SELECT * FROM sites WHERE id >= (SELECT floor(RAND() * (SELECT MAX(id) FROM sites)))  ORDER BY id LIMIT 1;"
    mycorsor.execute(sql)
    query_all = mycorsor.fetchall()
    for row in query_all:
        print(row)

    print("=================== 15.从第二条开始读取前 3 条记录： ===================")
    sql = "SELECT * FROM sites LIMIT 3 OFFSET 1"
    mycorsor.execute(sql)
    query_all = mycorsor.fetchall()
    for row in query_all:
        print(row)

    print("=================== 16.删除记录 ===================")
    sql = "DELETE FROM sites WHERE name = 'apple'"
    mycorsor.execute(sql)
    mydb.commit()
    delete_count = mycorsor.rowcount
    print("{}条记录删除".format(delete_count))

    print("=================== 17.为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义删除语句的条件： ===================")
    sql = "DELETE FROM sites WHERE name = %s"
    values = ("baidu",)
    mycorsor.execute(sql, values)
    mydb.commit()
    delete_count = mycorsor.rowcount
    print("{}条记录删除".format(delete_count))

    print("=================== 18.更新表数据 ===================")
    sql = "UPDATE sites SET NAME = 'QQ' WHERE name = 'Tencent'"
    mycorsor.execute(sql)
    mydb.commit()
    update_count = mycorsor.rowcount
    print("{}条记录被更新".format(update_count))

    print("=================== 18.更新表数据 ===================")
    sql = "UPDATE sites SET NAME = %s WHERE name = %s"
    values = ("Github", "github")
    mycorsor.execute(sql, values)
    mydb.commit()
    update_count = mycorsor.rowcount
    print("{}条记录被更新".format(update_count))

    print("=================== 19.删除表 ===================")
    sql = "DROP TABLE IF EXISTS sites"
    mycorsor.execute(sql)

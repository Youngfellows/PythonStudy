# coding=utf-8
import json
import traceback
import pymysql
import random


class PPyMySQL(object):
    '''使用pymysql操作数据库'''

    def __init__(self):
        object.__init__(self)

    def connectDB(self):
        '''打开数据库'''
        db_host = "192.168.249.144"
        user = "root"
        pwd = "3282"
        database = "python4"
        db = pymysql.connect(db_host, user, pwd, database, charset='utf8')
        return db

    def createTable(self, db):
        '''创建person表'''
        try:
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            # 使用 execute() 方法执行 SQL，如果表存在则删除
            drop_sql = "DROP TABLE IF EXISTS person;"
            cursor.execute(drop_sql)

            # 使用预处理语句创建表
            sql = """CREATE TABLE person(
              id INT AUTO_INCREMENT PRIMARY KEY,
              name CHAR(50) NOT NULL,
              age INT NOT NULL,
              address CHAR(50),
              salary REAL
              );"""
            cursor.execute(sql)
            db.commit()
            return True
        except:
            # 如果发生错误则回滚
            db.rollback()
        return False

    def delete(self, db):
        '''清空表数据'''
        try:
            cursor = db.cursor()
            sql = "DELETE FROM person;"
            cursor.execute(sql)
        except:
            pass

    def insert(self, db, person):
        '''向person表插入数据'''
        try:
            cursor = db.cursor()
            sql = "INSERT INTO person (name,age,address,salary) values ('{}','{}','{}','{}');".format(person['name'],
                                                                                                      person['age'],
                                                                                                      person['address'],
                                                                                                      person['salary'])
            # print(sql)
            cursor.execute(sql)
            db.commit()
            return True
        except:
            # 如果发生错误则回滚
            db.rollback()
        return False

    def query(self, db):
        '''查询'''
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM person WHERE salary > 5000;"
            cursor.execute(sql)
            quer_all = cursor.fetchall()
            person_list = []
            keys = ["id", "name", "age", "address", "salary"]
            for p in quer_all:
                person = dict(zip(keys, p))
                person_list.append(person)
            return person_list
        except:
            # 如果发生错误则回滚
            db.rollback()

    def update(self, db):
        '''更新'''
        try:
            cursor = db.cursor()
            sql = "UPDATE person set age = age + 10 WHERE address='beijing';"
            cursor.execute(sql)
            db.commit()
            return True
        except:
            # 如果发生错误则回滚
            db.rollback()
        return False

    def delete_person(self, db):
        '''删除'''
        try:
            cursor = db.cursor()
            sql = "DELETE FROM person WHERE age < %s;" % (30)
            cursor.execute(sql)
            db.commit()
            return True
        except:
            # 如果发生错误则回滚
            db.rollback()
        return False

    def closeDB(self, db):
        '''关闭数据库'''
        try:
            db.close()
        except:
            pass


if __name__ == "__main__":
    pp_mysql = PPyMySQL()
    # 1. 打开数据库
    db = pp_mysql.connectDB()

    # 2. 创建表
    pp_mysql.createTable(db)

    # 3. 先清空表
    pp_mysql.delete(db)

    # 3. 插入数据
    addrs = ["shenzhen", "beijing", "shanghai", "wuhan", "xiamen", "kunming", "nanling"]
    for index in range(100):
        name = "lili" + str(index)
        age = random.randint(1, 100)
        address = random.choice(addrs)
        salary = random.uniform(1, 10000)
        person = {"name": name, "age": age, "address": address, "salary": salary}
        pp_mysql.insert(db, person)

    # 4. 查询数据
    person_array = pp_mysql.query(db)
    print(person_array)

    # 5. 更新操作
    pp_mysql.update(db)

    # 6. 删除操作
    pp_mysql.delete_person(db)

    person_array = pp_mysql.query(db)
    print(person_array)

    # 7. 关闭数据库
    pp_mysql.closeDB(db)

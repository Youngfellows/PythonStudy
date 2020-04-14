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
    # 创建数据库
    mycorsor = mydb.cursor()
    # mycorsor.execute("create database python4")

    # 删除数据库
    # mycorsor.execute("use python4")
    # mycorsor.execute("create table person(name varchar(40),age int)")
    mycorsor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")

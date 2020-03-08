# coding=utf-8
import threading


class Studen:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


# 创建全局ThreadLocal对象:
local_school = threading.local()


# 获取当前线程关联的student:
def process_studen():
    stu = local_school.studen
    print("Hello,name:%s,age:%d,sex:%s,(in %s)" % (stu.name, stu.age, stu.sex, threading.current_thread().name))


# 绑定ThreadLocal的student:
def process_thread(studen):
    local_school.studen = studen
    process_studen()


if __name__ == "__main__":
    # laowang = Studen("老王", 33, "男")
    # zhaomin = Studen("赵敏", 23, "女")
    # t1 = threading.Thread(target=process_thread, args=("老王",), name="Thread-A")
    # t2 = threading.Thread(target=process_thread, args=("赵敏",), name="Thread-B")

    laowang = Studen("老王", 33, "男")
    zhaomin = Studen("赵敏", 23, "女")
    t1 = threading.Thread(target=process_thread, args=(laowang,), name="Thread-A")
    t2 = threading.Thread(target=process_thread, args=(zhaomin,), name="Thread-B")

    t1.start()
    t2.start()

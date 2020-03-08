# coding=utf-8
from threading import Thread, Lock
from time import sleep


# 创建线程1
class Task1(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            if lock1.acquire():
                print("----Task 1-----")
                sleep(0.5)
                lock2.release()


# 创建线程2
class Task2(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            if lock2.acquire():
                print("----Task 2-----")
                sleep(0.5)
                lock3.release()


# 创建线程3
class Task3(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            if lock3.acquire():
                print("----Task 3-----")
                sleep(0.5)
                lock1.release()


# 使用Lock创建出的锁默认没有“锁上”
lock1 = Lock()

# 创建另外一把锁，并且“锁上”
lock2 = Lock()
lock2.acquire()

# 创建另外一把锁，并且“锁上”
lock3 = Lock()
lock3.acquire()

t1 = Task1()
t2 = Task2()
t3 = Task3()

t1.start()
t2.start()
t3.start()

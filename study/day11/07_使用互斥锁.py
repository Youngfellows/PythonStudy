# coding=utf-8
from threading import Thread, Lock
import time

# 定义全局变量
g_num = 0


# 任务1
def task1():
    global g_num
    # 这个线程和task2线程都在抢着　对这个锁　进行上锁，如果有１方成功的上锁，那么导致另外
    # 一方会堵塞（一直等待）到这个锁被解开为止
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    # 用来对mutex指向的这个锁　进行解锁，，，只要开了锁，那么接下来会让所有因为
    # 这个锁　被上了锁　而堵塞的线程　进行抢着上锁
    mutex.release()
    print("---in task1,g_num is {}".format(g_num))


# 任务2
def task2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    mutex.release()
    print("---in task2,g_num is {}".format(g_num))


# 创建一把互斥锁，这个锁默认是没有上锁的
mutex = Lock()

# 启动线程1
t1 = Thread(target=task1())
t1.start()

# 启动线程2
t2 = Thread(target=task2())
t2.start()

print("---g_num is {}".format(g_num))

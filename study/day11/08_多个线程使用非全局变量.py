# coding=utf-8
from threading import Thread
import threading
import time


def task():
    # 注意：
    #   1. 全局变量在多个线程中　共享，为了保证正确运行需要锁
    #   2. 非全局变量在每个线程中　各有一份，不会共享，当然了不需要加锁
    name = threading.current_thread().name
    print("thread name is {}".format(name))
    number = 100
    if name == "Thread-1":
        number += 5
    else:
        time.sleep(3)

    print("--thread is {},number is {}".format(name, number))


if __name__ == "__main__":
    t1 = Thread(target=task)
    t1.start()

    t2 = Thread(target=task)
    t2.start()

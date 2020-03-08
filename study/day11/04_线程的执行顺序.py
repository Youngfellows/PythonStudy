# coding=utf-8
from threading import Thread
import time


# 创建自定义线程
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(7):
            time.sleep(1)
            msg = "I'm " + self.name + " @ " + str(i)
            print(msg)


def test():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == "__main__":
    test()

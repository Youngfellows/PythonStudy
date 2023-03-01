from threading import Thread
import time


# 创建自定义线程
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(5):
            time.sleep(1)
            # name属性中保存的是当前线程的名字
            msg = "\nI'm " + self.name + " @ " + str(i)
            print(msg, end="\n")


if __name__ == "__main__":
    t = MyThread()
    t.start()

    t = MyThread()
    t.start()

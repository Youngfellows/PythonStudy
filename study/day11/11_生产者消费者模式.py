# encoding=utf-8
from threading import Thread
from queue import Queue
import time


# 生产者
class Producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = "生成产品" + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.1)


# 消费者
class Consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + "消费了 " + queue.get()
                    print(msg)
            time.sleep(0.3)


if __name__ == "__main__":
    queue = Queue()

    for i in range(500):
        queue.put("初始产品" + str(i))

    # 创建3个生产者线程
    for i in range(3):
        p = Producer()
        p.start()

    # 创建5个消费者线程
    for i in range(5):
        c = Consumer()
        c.start()

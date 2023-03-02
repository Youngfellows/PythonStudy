# encoding=utf-8
import threading

num = 0  # 全局变量多个线程可以读写，传递数据
mutex = threading.Lock()  # 创建一个锁


class Mythread(threading.Thread):
    def run(self):
        global num
        # with mutex:  # with Lock的作用相当于自动获取和释放锁(资源)
        for i in range(1000000):  # 锁定期间，其他线程不可以干活，也
            num += 1  # 也就是说，with 的代码块同一时间只会有一个线程去执行
        print(num)


mythreads = []  # 线程列表
for i in range(5):
    t = Mythread()
    t.start()
    mythreads.append(t)
for t in mythreads:
    t.join()
print("game over")

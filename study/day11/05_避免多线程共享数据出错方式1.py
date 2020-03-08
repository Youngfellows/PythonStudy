# coding=utf-8
from threading import Thread
import time

# 线程之间共享全局变量
g_num = 0
g_flag = 1


def work1():
    global g_num
    global g_flag
    if g_flag == 1:
        for i in range(10000000):
            g_num += 1

    g_flag = 0
    print("----in work1,g_num is {}".format(g_num))


def work2():
    global g_num
    global g_flag
    print("----in work2, g_flag = {}".format(g_flag))
    while True:
        # print("------in work2-------{}".format((g_flag != 1)))
        if g_flag != 1:
            for i in range(10000000):
                g_num += 1

            # 计算完成结束死循环
            break
    print("----in work2,g_num is {}".format(g_num))


print("---线程创建之前,g_num is {}".format(g_num))

if __name__ == "__main__":
    t1 = Thread(target=work1())
    t1.start()

    # 延时一会儿,保证work1中的事情做完
    # time.sleep(1)

    t2 = Thread(target=work2())
    t2.start()

    print("---g_num=%d---" % g_num)

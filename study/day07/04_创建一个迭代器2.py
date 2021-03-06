"""
创建一个迭代器
    把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
    如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
    更多内容查阅：Python3 面向对象
    __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
    __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
"""


class MyNumber:
    def __init__(self):
        print("执行 __init__ 构造函数 ...")

    def __iter__(self):
        self.count = 1
        return self

    def __next__(self):
        if self.count < 20:
            next_element = self.count
            self.count += 1
            return next_element
        else:
            # 抛出异常
            raise StopIteration


myclass = MyNumber()
# 创建迭代器
my_iter = iter(myclass)

# 迭代元素
for ele in my_iter:
    print(ele)

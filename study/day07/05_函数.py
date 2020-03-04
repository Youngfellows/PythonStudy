# 1.定义函数
def say():
    print("welcom to china ...")


# 调用函数
say()


# 2.函数返回值
def sum(a, b):
    return a + b


print("sum = %d" % sum(3, 4))

print("*" * 30)


# 3.不可变参数
def changeInt(number):
    number = 3
    print("内部number: %d" % number)


number = 15
changeInt(15)
print("外面number: %d" % number)


# 4.可变参数
def changeme(mylist):
    mylist.append([1, 2, 3, 4, 5])
    print("函数内取值:", mylist)
    return


mylist = [33, 44, 55]
changeme(mylist)
print("函数外取值:", mylist)

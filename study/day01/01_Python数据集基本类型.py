# 1.基本数据类型
a = 1
b = 2000
c = -234
d = 0
e = 3.14
f = 0xff00
h = -9.8
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(h))

# 2.字符串类型
str1 = 'sheng zheng'
str2 = "china bei jing"
str3 = '''
你好,欢迎来深圳
这里是你的家
'''
print(type(str1))
print(str1)
print(str2)
print(str3)

# 字符串转义
str4 = '小明说\"我很好\"'
print(str4)

# 使用%操作符,和.format,使字符串格式化
name = "晓丽"
age = 18
size = 6
print("%s今天%d岁生日,哥哥给她买%d个蛋糕" % (name, age, size))
print("{0}今天{1}岁生日,哥哥给她买{2}个蛋糕".format(name, age, size))

# 3.布尔类型
isDel = True
isHot = False
print(type(isDel))
print(type(isHot))
print(isDel)
print(isHot)

# 4.空值
print(type(None))
print(type(0))
print(type(''))
print(None == 0)
print(None == '')
print(None == False)

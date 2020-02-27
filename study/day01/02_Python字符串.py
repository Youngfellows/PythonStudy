# 1.字符串的连接
str1 = '加油'
str2 = "武汉..."
str3 = str1 + str2
print(str3)

# 2.字符串的合并
urlList = ['www', 'google', 'com']
url = '.'.join(urlList)
print(url)

# 3.字符串相乘
line = "*" * 30
print(line)

# 4.字符串切片
# 字符串、列表、元组都支持切片操作，主要是在对象中截取一部分元素的操作
# 序列切片语法：序列[开始下标位置:结束下标位置:步长]
# 步长：步长的意思就是选取数据的间隔，默认为1，如果为负数，那么就是从后往前面开始截取,也就是有一个倒序开始截取

# 正数步长操作
str4 = "apple orange banana china ben"
subStr1 = str4[0:9]  # 取第1個到第9個字符你
print(subStr1)
subStr2 = str4[-6:]
print(subStr2)  # 从倒数第6个字符到字符串结束的字符
subStr3 = str4[-6:-4]
print(subStr3)  # 从倒数第6个字符到倒数第4个字符
subStr4 = str4[-6:-9]  # 从倒数第6个字符到倒数第9个字符,向右边开始截取,无法截取到字符
print(subStr4)

# 注意：截取的数据是不包含结束位置下标的数据
str5 = '0123456789'
subStr5 = str5[2:11:1]
print(subStr5)
subStr6 = str5[2:11:2]
print(subStr6)
subStr7 = str5[2:11]
print(subStr7)
subStr8 = str5[::2]
print(subStr8)
subStr9 = str5[2::]
print(subStr9)

# 负数步长操作
# 注意：如果选取方向（下标开始到结束的方向）和步长的方向冲突，将无法截取数据
str6 = "0123456789"
print(str6[11:0:-1])
print(str6[8:3:-2])
print(str6[-5:-1])

# 5.字符串的分割
# 普通的分割，用split
# split只能做非常简单的分割，而且不支持多个分隔
phone = '400-800-8888-1345'
phoneResult = phone.split('-')  # 分割结果是列表
print(phoneResult)

# 复杂的分割,正则表达式
# r表示不转义,分隔符可以是;或者,或者空格后面跟0个多个额外的空格，然后按照这个模式去分割
import re

line = "hello world;python, I ,like,     it"
reResult = re.split(r'[;,\t]+', line)
print(reResult)

line1 = 'abc aa;bb,cc | dd(xx).xxx 12.12        ssssss'
# 按空格切
print(re.split(r' +', line1))
# 加将空格放可选框内[]内
print(re.split(r'[ ]+', line1))

# 按所有空白字符来切割：\s（[\t\n\r\f\v]）\S（任意非空白字符[^\t\n\r\f\v]
print(re.split(r'[\s]+', line1))

# 多字符匹配
print(re.split(r'[\s;,.]+', line1))

# 使用括号捕获分组，默认保留分割符
print(re.split(r'([;])', line1))

# 去掉分隔符，加?:
print(re.split(r'(?:;)', line1))

# 6.字符串的开头和结尾的处理
fileName = 'apple.java'
print(fileName.startswith('apple2'))
print(fileName.endswith('.java'))

# 7. 字符串的查找和匹配
# 一般查找
# 我们可以很方便的在长的字符串里面查找子字符串，会返回子字符串所在位置的索引, 若找不到返回-1
title = 'python can be easy to pick up and powerful languages'
print(title.find("pick up"))

# 复杂的匹配,正则匹配

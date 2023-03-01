# coding=utf-8

if __name__ == "__main__":
    # 1. 两个列表(list)组成字典(dict)
    keys = ["name", "age", "sex", "city", "salary"]
    values = ["小龙女", "18", "女", "桃花岛", "1800"]
    print("type:%s" % type(zip(keys, values)))
    xiao_long_nv = dict(zip(keys, values))
    print("type(xiao_long_nv) = {}".format(type(xiao_long_nv)))
    print(xiao_long_nv)

    # 2.两个列表(list)组成字典(dict)\
    print("*" * 40)
    xiao_long_nv = {}
    for key, value in zip(keys, values):
        # print("{} : {}".format(key, value))
        xiao_long_nv[key] = value

    print(xiao_long_nv)

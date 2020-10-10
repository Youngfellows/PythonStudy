# coding=utf-8
import os
import re


class MyOS(object):
    def __init__(self):
        object.__init__(self)

    def test(self):
        print("判断该路径是否为目录：", os.path.isdir("E:\爬虫资源"))
        print("判断该路径是否为文件：", os.path.isfile("E:\爬虫资源"))

        # 返回指定的路径下包含的文件或文件夹的名字的列表
        # path = "E:\爬虫资源"
        # path = "."
        path = os.getcwd()  # 返回当前工作目录
        dirs = os.listdir(path)  # 获取所有文件和文件夹
        print(dirs)

        # 输出所有文件和文件夹
        for file in dirs:
            print(file)
            if os.path.isdir(file) and file == "png":
                print(file, "是目录")

        print("*" * 60)
        # 返回指定的路径下包含的文件或文件夹的名字的列表，还可以返回文件夹中文件名列表
        # gens = os.walk(path)
        # for parent, dirnames, filenames in gens:
        #     print(parent, dirnames, filenames)
        # parent：指目录下所有文件及文件夹的名称列表
        # dirname：文件夹的名字
        # filenames：列出了路径下所有的文件名称列表

        # 下面代码可获得指定路径下的所有文件及文件夹下子文件的目录列表
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                file = os.path.join(parent, filename)
                print(file)

    def rename_all(self):
        """批处理修改文件名称"""
        # path = "E:\爬虫资源"
        # path = "."
        path = os.getcwd()  # 返回当前工作目录
        dirs = os.listdir(path)  # 获取所有文件和文件夹
        print(dirs)
        number = 0

        print("*" * 60)
        # 输出所有文件和文件夹
        for file in dirs:
            print(file)
            if os.path.isdir(file) and file == "png":
                print("*" * 60)
                # print(file, "是目录")
                path = path + os.sep + "png"
                # print("path: ", path)

                # 获得指定路径下的所有文件及文件夹下子文件的目录列表
                for parent, dirnames, filenames in os.walk(path):
                    for filename in filenames:
                        # print("parent: {}, filename: {}".format(parent, filename))
                        file = os.path.join(parent, filename)
                        print(file)

                        # 获取文件后缀
                        index = filename.rfind(r".")  # 最后一次出现点的位置
                        name = filename[0:index]
                        file_suffix = filename[index:]
                        print("index:{}, name:{}, file_suffix:{}".format(index, name, file_suffix))
                        # new_name = re.sub(r"_\[.*\]_", "_[浪漫巴厘岛]_", name)
                        new_name = re.sub(r"^\d.*_+", "_[浪漫巴厘岛]_", name)
                        print("new_name: {}".format(new_name))
                        # new_file = parent + os.sep + str(number) + "_" + name + file_suffix
                        new_file = parent + os.sep + str(number) + new_name + file_suffix
                        print("new_file: {}".format(new_file))
                        os.rename(file, new_file)
                        number = number + 1


if __name__ == "__main__":
    myos = MyOS()
    myos.test()
    myos.rename_all()

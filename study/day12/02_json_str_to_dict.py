# coding=utf-8

import json
import os
from study.day12.file_path_manager import FilePathManager

jsondata = '''
{
"Uin":0,
"UserName":"@c482d142bc698bc3971d9f8c26335c5c",
"NickName":"小帅b",
"HeadImgUrl":"/cgi-bin/mmwebwx-bin/webwxgeticon?seq=500080&username=@c482d142bc698bc3971d9f8c26335c5c&skey=@crypt_b0f5e54e_b80a5e6dffebd14896dc9c72049712bf",
"DisplayName":"赵敏",
"ChatRoomId":0,
"KeyWord":"che",
"EncryChatRoomId":"",
"IsOwner":0
}
'''


def json2dict(json_data):
    """将json字符串转化为python的字典对象"""
    return json.loads(json_data)


def read2json(file_name):
    """读取json文件,并转换为字典/列表"""
    with open(file_name, "r", encoding="utf-8") as fp:
        dict = json.load(fp)
    print(dict)
    return dict


def writer2json(file_name, dict):
    """将字典对象保存为json字符串"""
    # 删除旧文件
    if file_name in os.listdir():
        os.remove(file_name)

    # dumps()默认中文为ascii编码格式，ensure_ascii默认为Ture
    # 禁用ascii编码格式，返回的Unicode字符串，方便使用
    json_str = json.dumps(dict, ensure_ascii=False)
    with open(file_name, "wb") as fp:
        fp.write(json_str.encode('utf-8'))


if __name__ == "__main__":
    # 将json字符串转化为python的字典对象
    my_friend = json2dict(jsondata)
    print("{} : {}".format(my_friend["NickName"], my_friend["DisplayName"]))

    file_manager = FilePathManager()
    file_manager.mkdir("/json/")

    file_name = "./json/my_friend.json"

    # 将字典对象保存为json字符串
    writer2json(file_name, my_friend)

    # 读取json文件, 并转换为字典 / 列表
    my_friend = read2json(file_name)
    print("{} : {}".format(my_friend["NickName"], my_friend["DisplayName"]))

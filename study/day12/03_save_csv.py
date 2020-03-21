# coding=utf-8

import csv
import pandas as pd

if __name__ == "__main__":
    # 保存到.csv文件
    with open("./json/xiaoshuaibi.csv", "w", encoding="utf-8") as csv_file:
        field_names = ["你是谁", "你几岁", "你多高"]
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerow({"你是谁": "赵敏", "你几岁": "18", "你多高": "180cm"})
        writer.writerow({"你是谁": "杨过", "你几岁": "22", "你多高": "170cm"})
        writer.writerow({"你是谁": "小龙女", "你几岁": "18", "你多高": "165cm"})
        writer.writerow({"你是谁": "张无忌", "你几岁": "33", "你多高": "180cm"})
        writer.writerow({"你是谁": "赵敏", "你几岁": "18", "你多高": "180cm"})

    # 读取.csv文件
    xiaoshuaibi = pd.read_csv("./json/xiaoshuaibi.csv")
    print(xiaoshuaibi)

    # 用 pandas 来存储 CSV 数据
    b = ['小帅b', '小帅c', '小帅d']
    c = ['18岁', '19岁', '20岁']
    d = ['18cm', '17cm', '16cm']

    df = pd.DataFrame({'你是谁': b, '你几岁': c, '你多高': d})
    df.to_csv("./json/xsb.csv", index=False, sep=',')
# coding=utf-8
from datetime import *
import math


class Calendar(object):
    """
    儒略日、公历年月日之间的转换以及儒略日的应用
    """

    def __init__(self):
        object.__init__(self)
        self.dizhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        self.ke = ['初', '一', '二', '三', '四']

    def ce2jd(self, Year, Month, D):
        """
        公历转儒略日: 比如2020年11月1日 12:0::0: ==>>> 2459155,默认周的开始日期是周日
        :param Year: 公历年
        :param Month: 公历月
        :param D:公历日
        :return:返回儒略日
        """
        if Month in [1, 2]:
            M = Month + 12
            Y = Year - 1
        else:
            Y = Year
            M = Month
        B = 0
        if Y > 1582 or (Y == 1582 and M > 10) or (Y == 1582 and M == 10 and D >= 15):
            B = 2 - int(Y / 100) + int(Y / 400)  # 公元1582年10月15日以后每400年减少3闰
        JD = math.floor(365.25 * (Y + 4716)) + int(30.6 * (M + 1)) + D + B - 1524.5
        # JD = math.floor(365.25*(Y+4712))+int(30.6*(M+1))+D+B-63.5
        print("{}年{}月{}日的儒略日为：{:.5f}".format(self.gyjn(Year), Month, D, JD))
        if Y > 1858 or (Y == 1858 and M > 11) or (Y == 1858 and M == 11 and D >= 17):
            MJD = int(JD - 2400000.5)
            print("简化儒略日为：{}".format(MJD))
        return JD

    def gyjn(self, year):
        """
        将天文计算年份表达为公元纪年法年份的函数
        :param year:
        :return:
        """
        if year > 1:
            ce = "公元" + str(year)
        elif year == 1:
            ce = "公元元"
        elif year <= 0:
            year -= 1
            ce = "公元前" + str(-year)
        return ce

    def jd2ce(self, JD):
        """
        儒略日转公历
        :param JD: 儒略日
        :return: 返回公历
        """

        JD = JD + 0.5  # 以BC4713年1月1日0时为历元
        Z = math.floor(JD)
        F = JD - Z  # 日的小数部分
        if Z < 2299161:  # 儒略历
            A = Z
        else:  # 格里历
            a = math.floor((Z - 2305447.5) / 36524.25)
            A = Z + 10 + a - math.floor(a / 4)
        k = 0
        while True:
            B = A + 1524  # 以BC4717年3月1日0时为历元
            C = math.floor((B - 122.1) / 365.25)  # 积年
            D = math.floor(365.25 * C)  # 积年的日数
            E = math.floor((B - D) / 30.6)  # B-D为年内积日，E即月数
            day = B - D - math.floor(30.6 * E) + F
            if day >= 1: break  # 否则即在上一月，可前置一日重新计算
            A -= 1
            k += 1
        month = E - 1 if E < 14 else E - 13
        year = C - 4716 if month > 2 else C - 4715
        day += k
        if int(day) == 0: day += 1
        ce = self.gyjn(year)
        print("儒略日{}对应的公历日期为{}年{}月{}日".format(JD - 0.5, ce, month, day), '\n')
        return year, month, day

    def day2hms(self, day):  # 12h起算的日数转时分秒
        """
        24小时制
        :param day:
        :return:
        """
        day += 0.5
        d = day - math.floor(day)  # 取出一日的小数部分
        h = int(d * 24)
        m = int(round((d * 24 - h) * 60, 4))
        if m == 60:
            m = 0
            h += 1
        s = d * 86400 - h * 3600 - m * 60
        if abs(s) < 0.001: s = 0
        return h, m, round(s, 2)

    def day2sk(self, JD):  # 0h起算的日数转古时刻（百刻制）
        """
        12时辰制
        :param JD:
        :return:
        """
        d = JD - math.floor(JD)  # 取出一日的小数部分（<0.0000001超过输出位数）
        chen = round(d * 12 + 0.5, 14)  # 时辰从上一日23时起
        chen_h = int(chen)
        chen_k = round(d * 100 - int(d * 12) * 100 / 12, 14)  # 该时辰内的刻数
        if chen_k < 100 / 24:
            shike = self.dizhi[chen_h % 12] + '正' + self.ke[int(chen_k)] + '刻'
        else:
            chen_k -= 100 / 24
            shike = self.dizhi[chen_h % 12] + '初' + self.ke[int(chen_k)] + '刻'
        return shike


if __name__ == "__main__":
    print("====儒略日、公历年月日之间的转换====")
    # 示例：计算当前时间的儒略日
    calendar = Calendar()
    # 当前的公历法日期
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    # 将公历转化为儒略日
    calendar.ce2jd(year, month, day)

    # 儒略日转公历
    calendar.jd2ce(2400000.5)  # print：1858年11月17.0日（简化儒略日历元）
    calendar.jd2ce(2299160.5)  # print：1582年10月15.0日（格里历历元）
    calendar.jd2ce(2299160.5 - 1)  # print：1582年10月4.0日（儒略历最后一日）
    calendar.jd2ce(2459155)  # print：2020年11月1.5日（儒略历最后一日）
    calendar.jd2ce(2459155)  # print：2020年11月1.5日（儒略历最后一日）
    calendar.jd2ce(2459174)  # print：2020年11月20.5日（儒略历最后一日）

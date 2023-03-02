# coding=utf-8
import sys
import getopt


class CmdField(object):
    def __init__(self):
        object.__init__(self)

    def main(self, argv):
        """
        取得命令行参数: python.exe .\01_获取命令行参数.py -s xxx.apk -p yyy.apk
        """
        shield_path = ''
        payload_path = ''
        try:
            print("args:{}".format(argv))
            opts, args = getopt.getopt(argv, "hs:p:", ["shield_path=", "payload_path="])
        except getopt.GetoptError:
            print('-s <shield apk path>', '-p <payload apk path>')
            sys.exit(2)
        print("args:{}".format(args))
        print("opts:{}".format(opts))
        for opt, arg in opts:
            print("opt:%s,arg:%s" % (opt, arg))
            if opt == '-h':
                print("usage: python.exe 01_获取命令行参数.py -s <shield apk path> -p <payload apk path>")
                sys.exit()
            elif opt in ("-s", "--shield_path"):
                shield_path = arg
            elif opt in ("-p", "--payload_path"):
                payload_path = arg
        print("shield_path:{}".format(shield_path))
        print("payload_path:{}".format(payload_path))


if __name__ == "__main__":
    cmd_filed = CmdField()
    cmd_filed.main(argv=sys.argv[1:])

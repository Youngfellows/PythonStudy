# -*- coding: UTF-8 -*-
import argparse

if __name__ == "__main__":
    """
    获取命令行参数:  python .\04_argparse.py -h
                  python .\04_argparse.py 1 2 3 4
    """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print("args:{}".format(args))
    print(args.accumulate(args.integers))

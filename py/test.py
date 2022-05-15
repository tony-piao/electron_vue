# coding: UTF-8
import sys

def add(a, b):
    print('第一个参数', a)
    print('第一个参数', b)

if __name__ == '__main__':
	arg1, arg2 = sys.argv[1], sys.argv[2]   # 接收位置参数
	add(arg1, arg2)
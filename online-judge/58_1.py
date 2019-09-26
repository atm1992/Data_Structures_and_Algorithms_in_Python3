#-*- coding: UTF-8 -*-

import sys


def sys_convert(n):
    """进制转换。十进制转换为27进制"""
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '\\', '<', '>', '?']
    if n < 0:
        a = -n
        result = '-'
    elif n == 0:
        a = n
        result = '0'
    else:
        a = n
        result = ''
    numbers = []
    while a > 0:
        numbers.append(a % 27)
        a = a // 27
    num_size = len(numbers)
    if num_size > 0:
        for i in range(num_size - 1, -1, -1):
            result += chars[numbers[i]]
    print(result)


if __name__ == '__main__':
    # n = int(sys.stdin.readline().strip())
    sys_convert(-236)

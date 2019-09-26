#-*- coding: UTF-8 -*-
"""
汉诺塔问题：古代有一个梵塔，塔内有三个座A、B、C，A座上有64个盘子，
盘子大小不等，大的在下，小的在上。有一个和尚想把这个盘子从A座移到B座，
但每次只能允许移动一个盘子，并且在移动过程中，3个座上的盘子始终保持大盘在下，小盘在上。
"""


def hanoi_tower(n, a, b, c):
    """用递归求解汉诺塔问题"""
    # 输入的n小于1时，直接返回，不进行任何操作
    if n < 1:
        return
    # 递归返回条件
    if n == 1:
        print(a + " ---> " + c)
    # 这里要用else，是因为写的print，并没有使用return返回
    else:
        # 下面的递归代码包含了两个及以上盘子的情况，
        # 所以递归返回只需考虑两个以下盘子的情况
        hanoi_tower(n - 1, a, c, b)
        print(a + " ---> " + c)
        hanoi_tower(n - 1, b, a, c)


if __name__ == '__main__':
    hanoi_tower(-1, 'A', 'B', 'C')
    hanoi_tower(2, 'A', 'B', 'C')

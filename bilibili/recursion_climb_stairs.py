#-*- coding: UTF-8 -*-
"""
一个人爬台阶，每次只能爬1个或2个台阶，假设有n个台阶，那么这个人有多少种不同的爬台阶方法？
"""


def climb_stairs(n):
    """
    用递归求解爬台阶问题。
    问题可分为两类：
        第一类：第一步走了一个台阶，然后再走 n-1 个台阶
        第二类：第一步走了两个台阶，然后再走 n-2 个台阶
    """
    # climb_stairs(n) = climb_stairs(n-1) + climb_stairs(n-2)
    # 若台阶数少于1，则直接返回，不进行任何操作
    if n < 1:
        return
    # 若只有1个台阶，则只有一种走法（爬1个台阶）
    if n == 1:
        return 1
    # 若有2个台阶，则有2种走法（爬两次1个台阶、爬一次2个台阶）
    if n == 2:
        return 2
    # 下面的递归代码包含了三个及以上台阶的情况（因为n-2要大于0），
    # 所以递归返回只需考虑三个以下台阶的情况
    return climb_stairs(n-1) + climb_stairs(n-2)


if __name__ == '__main__':
    print("爬3个台阶的走法有：", climb_stairs(3))

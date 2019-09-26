#-*- coding: UTF-8 -*-


def list_sum(alist):
    """用递归进行数组求和"""
    n = len(alist)
    # 若数组为空，则直接返回，不做任何操作
    if n == 0:
        # 等价于 return None
        return
    # 递归返回条件
    if n == 1:
        return alist[0]
    # 将输入数组划分为两部分：第一个元素、后面剩余的所有元素（看作一个整体）
    # 问题简化为只有两个元素：第一个元素 加上 后面剩余的所有元素之和 就得到了最终结果
    # 下面的递归代码包含了两个及以上元素的情况，所以递归返回只需考虑两个以下元素的情况
    return alist[0] + list_sum(alist[1:])


if __name__ == '__main__':
    a = []
    b = [0]
    c = [1, -2, 3]
    print(str(a) + " 求和结果：", list_sum(a))
    print(str(b) + " 求和结果：", list_sum(b))
    print(str(c) + " 求和结果：", list_sum(c))

#-*- coding: UTF-8 -*-


def shell_sort(alist):
    """
    希尔排序，插入排序的改进版。
    可对顺序表进行排序，也可对链表进行排序。
    此处选择输入一个顺序表，使用Python自带的list。
    若输入的是一个链表，则排序过程中通过修改节点的链接域来实现元素的交换位置
    """
    print("希尔排序前：", alist)
    n = len(alist)
    # 初始增量gap
    gap = n // 2
    # 整个排序过程中的位置交换次数
    change_count = 0
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, gap - 1, -gap):
                if alist[j - gap] > alist[j]:
                    change_count += 1
                    # Python中的变量交换
                    alist[j], alist[j - gap] = alist[j - gap], alist[j]
                else:
                    # 减少不必要的比较次数，并不会减少元素的交换次数
                    break
        gap //= 2
    print("整个排序过程总共进行了 " + str(change_count) + " 次位置交换")
    print("希尔排序后：", alist)
    print("")
    # 并不需要返回alist，因为传入的是引用
    # return alist


if __name__ == '__main__':
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    b = [1, 2, 3, 4, 5, 6]
    c = [1]
    # list为空，并不会报错。因为list(range(0, 0)) 为 []，并不进入for循环
    d = []
    e = [4, 3, 3, 4, 5, 6]
    shell_sort(a)
    shell_sort(b)
    shell_sort(c)
    shell_sort(d)
    shell_sort(e)

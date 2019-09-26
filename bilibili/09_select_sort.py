#-*- coding: UTF-8 -*-


def select_sort(alist):
    """
    选择排序。
    可对顺序表进行排序，也可对链表进行排序。
    此处选择输入一个顺序表，使用Python自带的list。
    若输入的是一个链表，则排序过程中通过修改节点的链接域来实现元素的交换位置
    """
    print("选择排序前：", alist)
    n = len(alist)
    # 整个排序过程中的位置交换次数
    change_count = 0
    for j in range(n - 1):
        # min_index用于记录此次排序过程中最小元素的下标
        min_index = j
        for i in range(j + 1, n):
            if alist[i] < alist[min_index]:
                min_index = i
        if min_index != j:
            change_count += 1
            # Python中的变量交换
            alist[j], alist[min_index] = alist[min_index], alist[j]
    print("整个排序过程总共进行了 " + str(change_count) + " 次位置交换")
    print("选择排序后：", alist)
    print("")
    # 并不需要返回alist，因为传入的是引用
    # return alist


if __name__ == '__main__':
    a = [7, 6, 5, 4, 3, 2, 1]
    b = [1, 2, 3, 4, 5, 6]
    c = [1]
    # list为空，并不会报错。因为list(range(-1)) 为 []，并不进入for循环
    d = []
    e = [4, 3, 3, 4, 5, 6]
    select_sort(a)
    select_sort(b)
    select_sort(c)
    select_sort(d)
    select_sort(e)

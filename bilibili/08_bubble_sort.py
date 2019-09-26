#-*- coding: UTF-8 -*-


def bubble_sort(alist):
    """
    冒泡排序。
    可对顺序表进行排序，也可对链表进行排序。
    此处选择输入一个顺序表，使用Python自带的list。
    若输入的是一个链表，则排序过程中通过修改节点的链接域来实现元素的交换位置
    """
    print("冒泡排序前：", alist)
    n = len(alist)
    # 总共进行的排序次数
    sort_count = 0
    for j in range(n - 1, 0, -1):
        # 此次排序过程中的交换位置次数
        change_count = 0
        sort_count += 1
        for i in range(j):
            # 若两个元素相等，则不进行交换。稳定性排序
            if alist[i] > alist[i + 1]:
                change_count += 1
                # Python中的变量交换
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        # 若此次排序没有发生交换位置，则退出循环，排序结束
        if change_count == 0:
            break
    print("总共进行了 " + str(sort_count) + " 次排序")
    print("冒泡排序后：", alist)
    # 并不需要返回alist，因为传入的是引用
    # return alist


if __name__ == '__main__':
    a = [7, 6, 5, 4, 3, 2, 1]
    b = [1, 2, 3, 4, 5, 6]
    c = [1]
    # list为空，并不会报错。因为list(range(-1, 0, -1)) 为 []，并不进入for循环
    d = []
    e = [4, 3, 3, 4, 5, 6]
    bubble_sort(a)
    bubble_sort(b)
    bubble_sort(c)
    bubble_sort(d)
    bubble_sort(e)

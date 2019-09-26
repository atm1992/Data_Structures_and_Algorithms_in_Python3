#-*- coding: UTF-8 -*-


def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    # 少于两个元素的话，不需要排序。递归的返回条件
    # 注意：这里每次返回的都是传入的新列表，而不是快速排序中的None
    if n < 2:
        return alist
    # 对所有待排序元素进行对半切
    mid = n // 2
    # 这里使用的递归。首先对所有元素不断地进行对半切，切到最后，每个子序列中只有一个或零个元素
    # 然后递归返回（开始执行下面的子序列合并代码）。从前往后先将相邻的单元素子序列两两合并为有序的两元素子序列，
    # 然后再从前往后将相邻的两元素子序列两两合并为有序的四元素子序列，以此类推……
    # left_li是对原列表左半部分进行归并排序后，返回的有序新列表
    left_li = merge_sort(alist[:mid])
    # right_li是对原列表右半部分进行归并排序后，返回的有序新列表
    right_li = merge_sort(alist[mid:])

    # 将上述两个有序的子序列合并为一个新列表，然后返回结果
    # return merge(left_li,right_li)

    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    # 若左子序列中还存在剩余元素，则将这些元素都直接复制到result列表中
    result.extend(left_li[left_pointer:])
    # result += left_li[left_pointer:]
    result.extend(right_li[right_pointer:])
    # result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    b = [1, 2, 3, 4, 5, 6]
    c = [1]
    d = []
    e = [4, 3, 3, 4, 5, 6]
    print("归并排序前：", a)
    print("归并排序后：", merge_sort(a))
    print("归并排序前：", b)
    print("归并排序后：", merge_sort(b))
    print("归并排序前：", c)
    print("归并排序后：", merge_sort(c))
    print("归并排序前：", d)
    print("归并排序后：", merge_sort(d))
    print("归并排序前：", e)
    print("归并排序后：", merge_sort(e))

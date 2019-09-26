#-*- coding: UTF-8 -*-


def quick_sort(alist, **kwargs):
    """快速排序"""
    if 'start' not in kwargs:
        print("快速排序前：", alist)
    n = len(alist)
    start = kwargs['start'] if 'start' in kwargs else 0
    end = kwargs['end'] if 'end' in kwargs else (n - 1)
    # 少于两个元素的话，不需要排序。递归的返回条件
    if n < 2 or (end - start) < 1:
        return None
    # 中间值，用于进行比较的基准值。默认使用list的第一个元素，当然也可使用其它元素
    mid = start
    # 从前往后（从左往右）移动
    left = start
    # 从后往前（从右往左）移动
    right = end
    # 为了避免每次进行比较时，都要从数列中查找获取该元素值
    mid_value = alist[mid]

    while left < right:
        # 下面这两个while循环不能交换位置
        # 退出循环时，right一定是停留在小于等于mid_value的那个元素所在位置
        while left < right and alist[right] > mid_value:
            right -= 1
        # 暂不考虑left >= right。退出循环时，left停留在大于mid_value的那个元素所在位置
        while left < right and alist[left] <= mid_value:
            left += 1
        if left < right:
            # 这里只是交换元素值，left 和 right所指向的位置是不变的
            # 交换完之后，left 和 right所指向的元素值又都满足进入上面那两个while循环的条件了
            alist[left], alist[right] = alist[right], alist[left]
    # 由于left和right这两个指针变量始终都是每次只移动其中一个，然后再判断left是否小于right
    # 所以退出上述循环时，一定是left等于right，不可能出现left大于right的情况
    # 并且left和right同时指向的该元素值一定是小于等于mid_value
    # 交换left、mid这两个位置的元素值
    alist[left], alist[mid] = alist[mid], alist[left]
    # 更新mid指针变量的值，mid所指向的元素已经找到了最终的排序位置
    mid = left
    # 使用递归对mid左右两边的子序列进行快速排序
    quick_sort(alist, start=start, end=(mid - 1))
    quick_sort(alist, start=(mid + 1), end=end)
    if 'start' not in kwargs:
        print("快速排序后：", alist)
        print("")
    # 并不需要返回alist，因为传入的是引用
    # return alist


if __name__ == '__main__':
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    b = [1, 2, 3, 4, 5, 6]
    c = [1]
    d = []
    e = [4, 3, 3, 4, 5, 6]
    quick_sort(a)
    quick_sort(b)
    quick_sort(c)
    quick_sort(d)
    quick_sort(e)

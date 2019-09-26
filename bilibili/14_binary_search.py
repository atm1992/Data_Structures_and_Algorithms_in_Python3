#-*- coding: UTF-8 -*-


# alist已按升序排列
def binary_search_recursion(item, alist, *args):
    """二分查找，递归实现"""
    start = args[0] if args else 0
    # 此处的len(alist)只有第一次才会去计算，其后都不需要用到
    end = args[1] if args else (len(alist) - 1)
    # 递归终止条件
    if start > end:
        return -1
    mid = (start+end) // 2
    if alist[mid] == item:
        return mid
    elif alist[mid] > item:
        # 这里一定要return，否则会接收不到递归的返回值，从而导致最终结果为None
        return binary_search_recursion(item, alist, start, mid - 1)
    else:
        # 这里一定要return，否则会接收不到递归的返回值，从而导致最终结果为None
        return binary_search_recursion(item, alist, mid + 1, end)


# alist已按升序排列
def binary_search_non_recursion(item, alist):
    """二分查找，非递归实现"""
    n = len(alist)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start+end) // 2
        if alist[mid] == item:
            return mid
        elif alist[mid] > item:
            end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    item = 1
    result_recursion = binary_search_recursion(item, a)
    if result_recursion != -1:
        print("递归版 —— 待查找元素 {} 在列表 {} 中的下标为：{}".format(item, a, result_recursion))
    else:
        print("递归版 —— 待查找元素 {} 在列表 {} 中未找到".format(item, a))

    result_non_recursion = binary_search_non_recursion(item, a)
    if result_non_recursion != -1:
        print("非递归版 —— 待查找元素 {} 在列表 {} 中的下标为：{}".format(item, a, result_non_recursion))
    else:
        print("非递归版 —— 待查找元素 {} 在列表 {} 中未找到".format(item, a))

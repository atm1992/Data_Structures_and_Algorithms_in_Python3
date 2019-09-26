#-*- coding: UTF-8 -*-

import sys


def quick_sort(alist, start, end):
    if (end - start) < 1:
        return
    left = start
    right = end
    mid_value = alist[start]

    while left < right:
        while left < right and alist[right] > mid_value:
            right -= 1
        while left < right and alist[left] <= mid_value:
            left += 1
        if left < right:
            alist[left], alist[right] = alist[right], alist[left]
    alist[left], alist[start] = mid_value, alist[left]
    quick_sort(alist, start, left - 1)
    quick_sort(alist, left + 1, end)


def run():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    li_1 = list(map(int, s1.split()))
    n, k = li_1[0], li_1[1]
    li_2 = list(map(int, s2.split()))
    quick_sort(li_2, 0, n - 1)
    accumulator = 0
    li_index = 0
    for i in range(k):
        while li_index < n and (li_2[li_index] - accumulator) <= 0:
            li_index += 1

        if li_index >= n:
            print(0)
        else:
            print(li_2[li_index] - accumulator)
            accumulator = li_2[li_index]


if __name__ == "__main__":
    run()

#-*- coding: UTF-8 -*-

import sys


def bubble_sort(alist, n):
    for j in range(n - 1, 0, -1):
        change_count = 0
        for i in range(j):
            if alist[i] > alist[i + 1]:
                change_count += 1
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        if change_count == 0:
            break


def run():
    n = int(sys.stdin.readline().strip())
    total = n
    s = sys.stdin.readline().strip()
    li = list(map(int, s.split()))
    bubble_sort(li, n)
    if total % 2 != 0:
        mid_value = li.pop(n // 2)
        n -= 1
    mid = n // 2
    odd_val, even_val = 0, 0
    for m in range(mid):
        if m % 2 == 0:
            odd_val += li[m] + li[n - 1 - m]
        else:
            even_val += li[m] + li[n - 1 - m]
    if total % 2 != 0:
        if odd_val <= even_val:
            odd_val += mid_value
        else:
            even_val += mid_value
    if odd_val <= even_val:
        print(odd_val, even_val)
        return odd_val, even_val
    else:
        print(even_val, odd_val)
        return even_val, odd_val


if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for k in range(t):
        run()

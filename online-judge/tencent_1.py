#-*- coding: UTF-8 -*-

import sys


def run():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    if n < 8:
        print("NO")
        return "NO"
    if s.find('8', 0, n - 8) == -1:
        print("NO")
        return "NO"
    print("YES")
    return "YES"


if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        run()

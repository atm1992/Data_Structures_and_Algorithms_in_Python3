#-*- coding: UTF-8 -*-

from timeit import Timer
"""
Python 中各种数据类型的内建函数并不是基本操作，而是Python语言替我们封装好的方法。
其实大部分内建函数的时间复杂度都不是O(1)
"""


def test1():
    li = []
    for i in range(10000):
        li = li + [i]    # 和 li += [i] 的时间复杂度并不一样


def test2():
    li = []
    for i in range(10000):
        li.append(i)


def test3():
    li = [i for i in range(10000)]


def test4():
    li = list(range(10000))


# extend 和 append的区别是，extend可以一次性加载另一个list中的所有元素，而append只能一个一个的元素追加
def test5():
    li = []
    for i in range(10000):
        li.extend([i])


# insert 是在列表头部插入元素，速度更慢
def test6():
    li = []
    for i in range(10000):
        li.insert(0, i)


if __name__ == '__main__':
    timer1 = Timer('test1()', 'from __main__ import test1')
    print('+  ', timer1.timeit(number=10000), "seconds")
    timer2 = Timer('test2()', 'from __main__ import test2')
    print('append  ', timer1.timeit(number=10000), "seconds")
    timer3 = Timer('test3()', 'from __main__ import test3')
    print('列表生成式  ', timer1.timeit(number=10000), "seconds")
    timer4 = Timer('test4()', 'from __main__ import test4')
    print('工厂函数+可迭代对象  ', timer1.timeit(number=10000), "seconds")
    timer5 = Timer('test5()', 'from __main__ import test5')
    print('extend  ', timer1.timeit(number=10000), "seconds")
    timer6 = Timer('test6()', 'from __main__ import test6')
    print('insert  ', timer1.timeit(number=10000), "seconds")

    x = list(range(2000000))
    # 列表头部pop元素
    pop_zero = Timer("x.pop(0)", "from __main__ import x")
    print("pop_zero ", pop_zero.timeit(number=1000), "seconds")

    y = list(range(2000000))
    # 列表尾部pop元素，很明显尾部要快很多
    pop_end = Timer("y.pop()", "from __main__ import y")
    print("pop_end ", pop_end.timeit(number=1000), "seconds")

#-*- coding: UTF-8 -*-


class Deque(object):
    """双端队列。可使用顺序表来实现，也可使用链表来实现。此处选择顺序表来实现，使用Python自带的list"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队头加入一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """往队尾加入一个item元素"""
        self.__list.append(item)

    def remove_front(self):
        """从队头删除一个元素"""
        if self.is_empty():
            return None
        return self.__list.pop(0)

    def remove_rear(self):
        """从队尾删除一个元素"""
        if self.is_empty():
            return None
        return self.__list.pop()

    def is_empty(self):
        """判断双端队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    dq = Deque()
    dq.add_front(1)
    dq.add_rear(2)
    dq.add_front(3)
    print("size:", dq.size())
    print(dq.remove_front())
    print(dq.remove_rear())
    print("size:", dq.size())
    print(dq.remove_rear())
    print(dq.remove_front())

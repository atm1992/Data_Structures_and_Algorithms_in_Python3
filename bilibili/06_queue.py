#-*- coding: UTF-8 -*-


class Queue(object):
    """队列。可以使用顺序表来实现，也可以使用链表来实现。此处选择顺序表来实现，使用Python自带的list"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列尾部添加一个item元素"""
        self.__list.append(item)
        # 往list头部插入元素，时间复杂度为O(n)
        # self.__list.insert(0, item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        # 判断队列是否为空
        if self.is_empty():
            return None
        return self.__list.pop(0)
        # 若前面是从头部插入元素，则这里必须从尾部删除元素
        # 根据业务需求去选择，若频繁插入元素，则选择list尾部追加元素；若频繁删除元素，则选择此方式，在list尾部删除元素
        # 从list尾部删除元素，时间复杂度为O(1)
        # self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("size:", q.size())
    print(q.dequeue())
    print(q.dequeue())
    print("size:", q.size())
    print(q.dequeue())
    print(q.dequeue())

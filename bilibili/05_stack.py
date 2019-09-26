#-*- coding: UTF-8 -*-


class Stack(object):
    """栈。可以使用顺序表来实现，也可以使用链表来实现。此处选择顺序表来实现，使用Python自带的list"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        if self.is_empty():
            return None
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        # 判断栈是否为空
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []
        # return not self.__list

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("size:", s.size())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print("size:", s.size())

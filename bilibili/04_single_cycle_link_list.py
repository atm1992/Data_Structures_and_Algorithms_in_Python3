# -*- coding: UTF-8 -*-


class SingleNode(object):
    """单链表节点"""
    def __init__(self, item):
        # elem存放数据元素
        self.elem = item
        # next存放下一个节点的标识
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        # 初始化单向循环链表，默认值为None，便于创建空链表
        self.__head = node
        # 若node不为None,则将next指向头节点。若为默认值None，则不进行任何操作
        if node:
            node.next = self.__head

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """返回链表长度"""
        if self.is_empty():
            return 0
        # 游标cur 刚开始和 __head一样，都指向链表中的第一个节点
        cur = self.__head
        # count从1开始计数，因为cur到达最后一个节点时退出循环，此时不会进入循环进行加1操作
        count = 1
        # cur.next == self.__head时退出循环；而不能使用cur != self.__head作为循环条件，
        # 因为cur的初始值就为self.__head，否则不能进入循环
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        # 若链表为空，则不进行任何操作，直接返回
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # cur指向尾结点时，退出上述while循环，因此要在最后打印尾结点信息
        print(cur.elem)

    def add(self, item):
        """在链表头部添加元素，头插法"""
        node = SingleNode(item)

        # node.next = self.__head
        # self.__head = node
        # cur = self.__head
        # # cur.next表示原链表为空，cur是刚插入的新node
        # # 会陷入死循环，cur.next永远不会等于self.__head
        # # 因为self.__head指向了新加入的node，而原链表的尾结点指向的是新加入node的后一个节点
        # while cur.next and cur.next != self.__head:
        #     cur = cur.next
        # cur.next = node

        # 处理原链表为空的特殊情况
        if self.is_empty():
            self.__head = node
            node.next = node
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """在链表尾部添加元素，尾插法"""
        node = SingleNode(item)
        # 考虑空链表的情况，空链表没有next属性
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos 从0开始，0代表头结点，原来的pos位置节点向后移
        """

        # 等价于头插法
        if pos <= 0:
            self.add(item)
        # 等价于尾插法
        elif pos >= self.length():
            self.append(item)
        # 在链表中间插入节点
        else:
            count = 0
            pre = self.__head
            # count == pos-1的时候，跳出循环，游标pre在pos-1的位置插入后一个节点，原来的pos位置节点向后移
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node = SingleNode(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点。若链表中存在多个等于item的节点，则只删除第一个"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        # 如果最后也没找到item，则不做任何操作
        while cur.next != self.__head:
            if cur.elem == item:
                # 若待删除节点为头节点
                if cur == self.__head:
                    # 这里不能先修改self.__head，否则下面的while循环会出问题
                    # self.__head = cur.next
                    rear = self.__head
                    # 让rear直接到达尾节点的位置
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = cur.next
                # 若待删除节点为中间节点
                else:
                    pre.next = cur.next
                cur.next = None
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:
            # 链表中只有一个头节点，并且头节点等于待删除item
            if cur == self.__head:
                self.__head = None
                cur.next = None
            else:
                # 正好尾节点为待删除节点
                pre.next = self.__head
                cur.next = None

    def search(self, item):
        """查找节点是否存在。时间复杂度O(n)"""
        # 若链表为空，则直接返回false
        if self.is_empty():
            print("sorry,not in")
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                print("yes,it's in")
                return True
            cur = cur.next
        # 此时的cur表示尾节点
        if cur.elem == item:
            print("yes,it's in")
            return True
        # 其余情况
        print("sorry,not in")
        return False


if __name__ == '__main__':
    scll = SingleCycleLinkList()
    print(scll.is_empty())
    print(scll.length())
    scll.append(2)
    scll.append(5)
    scll.add(9)
    scll.append(8)
    scll.travel()
    scll.insert(-1, -1)
    scll.travel()
    scll.insert(scll.length(), scll.length() + 1)
    scll.travel()
    print(scll.search(5))
    scll.insert(-100, 8)
    scll.travel()
    scll.remove(8)
    scll.travel()
    scll.remove(8)
    scll.travel()

# -*- coding: UTF-8 -*-


class SingleNode(object):
    """单链表节点"""
    def __init__(self, item):
        # elem存放数据元素
        self.elem = item
        # next存放下一个节点的标识
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        # 初始化单链表，默认值为None，便于创建空链表
        self.__head = node

    def is_empty(self):
        """判断单链表是否为空"""
        return self.__head is None

    def length(self):
        """返回链表长度"""
        # 游标cur 刚开始和 __head一样，都指向链表中的第一个节点
        cur = self.__head
        count = 0
        # 需要考虑空链表的情况
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        # 需要考虑空链表的情况
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")    # 换行

    def add(self, item):
        """在链表头部添加元素，头插法。时间复杂度O(1)"""
        node = SingleNode(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """在链表尾部添加元素，尾插法。时间复杂度O(n)"""
        node = SingleNode(item)
        # 考虑空链表的情况，空链表没有next属性
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素。时间复杂度O(n)
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
        cur = self.__head
        pre = None
        # 如果最后也没找到item，则不做任何操作
        while cur is not None:
            if cur.elem == item:
                # 如果待删除节点为头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                cur.next = None
                return
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在。时间复杂度O(n)"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                print("yes,it's in")
                return True
            cur = cur.next
        print("sorry,not in")
        return False


if __name__ == '__main__':
    sll = SingleLinkList()
    print(sll.is_empty())
    print(sll.length())
    sll.append(2)
    sll.append(5)
    sll.add(9)
    sll.append(8)
    sll.travel()
    sll.insert(-1, -1)
    sll.travel()
    sll.insert(sll.length(), sll.length() + 1)
    sll.travel()
    print(sll.search(5))
    sll.insert(-100,8)
    sll.travel()
    sll.remove(8)
    sll.travel()
    sll.remove(8)
    sll.travel()

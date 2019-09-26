#-*- coding: UTF-8 -*-
"""通过扩充链表来表示二叉树"""


class Node(object):
    """节点类"""
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class BinaryTree(object):
    """二叉树类"""

    # 初始化一棵树。初始化时可传入一个Node作为根节点，也可不传
    def __init__(self, root=None):
        self.root = root

    # 向二叉树添加节点
    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        # 定义一个队列来存放树的节点
        # 以广度优先遍历（即 层次遍历）的方式向队尾追加节点
        # 从队头pop出最老的节点，然后执行之后的操作
        queue = [self.root]
        # 只要队列中还有待处理节点，就一直循环下去
        while queue:
            # 获取当前待处理节点
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度优先遍历（即 层次遍历）"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        """深度优先遍历 之 先序遍历。根节点、左子树/节点、右子树/节点"""
        # 递归终止条件
        if node is None:
            return
        # 先打印传入节点（根节点）的信息
        print(node.elem, end=" ")
        # 然后打印传入节点（根节点）的左子树上的所有节点的信息
        self.preorder(node.lchild)
        # 最后打印传入节点（根节点）的右子树上的所有节点的信息
        self.preorder(node.rchild)

    def inorder(self, node):
        """深度优先遍历 之 中序遍历。左子树/节点、根节点、右子树/节点"""
        # 递归终止条件
        if node is None:
            return
        # 先打印传入节点（根节点）的左子树上的所有节点的信息
        self.inorder(node.lchild)
        # 然后打印传入节点（根节点）的信息
        print(node.elem, end=" ")
        # 最后打印传入节点（根节点）的右子树上的所有节点的信息
        self.inorder(node.rchild)

    def postorder(self, node):
        """深度优先遍历 之 后序遍历。左子树/节点、右子树/节点、根节点"""
        # 递归终止条件
        if node is None:
            return
        # 先打印传入节点（根节点）的左子树上的所有节点的信息
        self.postorder(node.lchild)
        # 然后打印传入节点（根节点）的右子树上的所有节点的信息
        self.postorder(node.rchild)
        # 最后打印传入节点（根节点）的信息
        print(node.elem, end=" ")


if __name__ == '__main__':
    # 初始化二叉树的时候，传入一个根节点，也可不传
    tree = BinaryTree(Node(0))
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print("广度优先遍历（即 层次遍历）：", end="")
    tree.breadth_travel()
    print("\n深度优先遍历 之 先序遍历：", end="")
    tree.preorder(tree.root)
    print("\n深度优先遍历 之 中序遍历：", end="")
    tree.inorder(tree.root)
    print("\n深度优先遍历 之 后序遍历：", end="")
    tree.postorder(tree.root)

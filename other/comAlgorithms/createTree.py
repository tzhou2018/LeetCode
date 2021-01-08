# -*- coding:utf-8 -*-

'二叉树结点类'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# '列表创建二叉树'


def listCreatTree(root, llist, i):
    if i < len(llist):
        if llist[i] == '#':
            return None  ###这里的return很重要
        else:
            root = TreeNode(llist[i])
            # 往左递推
            root.left = listCreatTree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listCreatTree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  ###这里的return很重要
    return root


# 递归实现
# 先序遍历二叉树
n = 0


def preOrderBT(root):
    if not root:
        return None
    print(root.val, end='\t')
    preOrderBT(root.left)
    preOrderBT(root.right)


# 中序遍历二叉树
def midOrdBT(root):
    if not root:
        return None
    midOrdBT(root.left)
    print(root.val, end="\t")
    midOrdBT(root.right)


# 后序遍历二叉树
def postOrdBT(root):
    if not root:
        return None
    postOrdBT(root.left)
    postOrdBT(root.right)
    print(root.val, end='\t')


# 层次遍历
# 试题 61 按之字形顺序打印二叉树


# 非递归实现
class NoRecursion:
    # 先序遍历
    def preOrder(self, root):
        stack = []
        num = 0
        if root:
            stack.append(root)
            while stack:
                root = stack.pop()
                print(root.val, end='\t')
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)

    # 中序遍历
    def midOrder(self, root):
        stack = []
        if root:
            cur = root
            while cur or stack:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                print(cur.val, end='\t')
                cur = cur.right

    # 中序
    def midOrder1(self, root):
        stack = []
        if not root:
            return None
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                print(cur.val + " ")
                cur = cur.right

    # 后序遍历
    """
    二叉树的后序非递归遍历就比较难写，因为涉及到判断节点的访问状态…
    现在有个很巧妙的方法：
    前序：根->左->右
    后序：左->右->根
    那么可以把后序当作：根->右->左，然后再反转一下即可。
    """

    def postOrder(self, root):
        nodeList = []
        stack = []
        count = 0
        if root:
            stack.append(root)
            while stack:
                root = stack.pop()
                nodeList.append(root.val)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)

        nodeList.reverse()
        print('\n', nodeList)


if __name__ == '__main__':
    # llist = ['1', '2', '3', '#', '5', '6', '7', '8', '#', '10']
    llist = [1, 2, 3, "#", 5, 6, 7, "#", "#", 8, "#", 10]
    root = listCreatTree(None, llist, 0)
    p = root
    print(".............................")
    print("先序   中序  后序")
    preOrderBT(root)
    print()
    midOrdBT(root)
    print()
    postOrdBT(p)
    # print(root.val)
    # while root
    print("\n非递归。。。。。")
    NoRecursion().preOrder(root)
    print()
    NoRecursion().midOrder(root)
    NoRecursion().postOrder(root)

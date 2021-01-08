"""
@Time    : 2020/8/22 19:36
@FileName: 08-22test01-yfd.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


class TreeNode:
    def __init__(self, v):
        self.val = v
        self.right = None
        self.left = None


def createTree(root, llist, i):
    if i < len(llist):
        if llist[i] == "#":
            return None
        else:
            root = TreeNode(llist[i])
            root.left = createTree(root.left, llist, 2 * i + 1)
            root.right = createTree(root.right, llist, 2 * i + 2)
            return root
    return root


leaveNode = []


def proOrder(root):
    if not root:
        return None
    if not root.left and not root.right:
        leaveNode.append(root.val)
    proOrder(root.left)
    proOrder(root.right)


# 获取最左边元素
def getLeft(root):
    stack = []
    if root:
        cur = root
        while cur:
            stack.append(cur.val)
            cur = cur.left
    return stack


def getRight(root):
    stack = []
    if root:
        cur = root
        while cur:
            stack.append(cur.val)
            cur = cur.right
    return stack


if __name__ == '__main__':
    n = int(input().strip())
    llist = list(map(int, input().strip().split(" ")[:n]))
    # llist = [1]
    root = createTree(None, llist, 0)
    left = getLeft(root)
    # if len(left) >= 2:
    #     left = left[:-1]
    proOrder(root)
    # if len(leaveNode) >= 2:
    #     leaveNode = leaveNode[:-1]
    right = getRight(root)[::-1]

    # if len(right) >= 1:
    #     right = right[::-1][:-1]
    res = []
    res.extend(left)
    if left[-1] == leaveNode[0]:
        res.extend(leaveNode[1:])
    if leaveNode[-1] == right[0]:
        res.extend(right[1:-1])
    else:
        res.extend(right[:-1])
    for e in res:
        print(e, end=" ")

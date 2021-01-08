"""
@Time    : 2020/7/31 20:35
@FileName: 662widthOfBinaryTree.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方案1： 参考官方解法，记录最左边第一个结点出现的位置
class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        queue = [(root, 1, 0)]
        curDepth = 1
        res = 1
        left = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))
                if depth != curDepth:
                    curDepth = depth
                    left = pos
                res = max(res, pos - left + 1)
        return res


# 方案2 ： 层次遍历
class Solution2:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        curNodeList = [(root, 0)]
        res = 1
        while curNodeList:
            nextCurNode = []
            arr = []
            while curNodeList:
                node, pos = curNodeList.pop(0)
                if node.left:
                    nextCurNode.append((node.left, pos * 2))
                    arr.append(pos * 2)
                if node.right:
                    nextCurNode.append((node.right, pos * 2 + 1))
                    arr.append(pos * 2 + 1)
            curNodeList = nextCurNode[:]
            if arr:
                res = max(res, arr[-1] - arr[0] + 1)
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution2().widthOfBinaryTree(root))

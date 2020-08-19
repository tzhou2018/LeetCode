'''
@Time    : 2020/2/20 22:18
@FileName: 110isBalanced.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if abs(right - left) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 也可以这样写
class ReturenType:
    def __init__(self, isB, h):
        self.isB = isB
        self.h = h


class Solution2:
    def isBalanced(self, root, h):
        if not root:
            return ReturenType(True, h - 1)
        left = self.isBalanced(root.left, h + 1)
        if not left.isB:
            return ReturenType(False, left.h)
        right = self.isBalanced(root.right, h + 1)
        if not right.isB:
            return ReturenType(False, right.h)
        if abs(left.h - right.h) > 1:
            return ReturenType(False, max(left.h, right.h))
        return ReturenType(True, max(left.h, right.h))


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    print(Solution().isBalanced(head))
    print(Solution2().isBalanced(head, 1).isB)

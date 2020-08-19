'''
@Time    : 2020/2/24 15:10
@FileName: 111minDepth.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return left + right + 1
        return min(left, right) + 1


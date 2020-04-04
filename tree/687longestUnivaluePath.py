'''
@Time    : 2020/2/24 16:55
@FileName: 687longestUnivaluePath.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.path = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.path

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        leftPath = left + 1 if root.left and root.left.val == root.val else 0
        rightPath = right + 1 if root.right and root.right.val == root.val else 0
        self.path = max(self.path, leftPath + rightPath)
        return max(leftPath, rightPath)

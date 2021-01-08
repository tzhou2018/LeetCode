'''
@Time    : 2020/2/20 22:02
@FileName: 104maxDepth.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return (max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1)

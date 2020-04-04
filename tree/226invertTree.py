'''
@Time    : 2020/2/21 20:22
@FileName: 226invertTree.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root

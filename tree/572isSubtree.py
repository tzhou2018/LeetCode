'''
@Time    : 2020/2/23 10:01
@FileName: 572isSubtree.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        return self.isBoole(s, t) or self.isSubtree(s.left, t) or \
               self.isSubtree(s.right, t)

    def isBoole(self, root1, root2):
        if not root2 and not root1:
            return True
        if not root2 or not root1:
            return False
        if root1.val != root2.val:
            return False
        return self.isBoole(root1.left, root2.left) and \
               self.isBoole(root1.right, root2.right)

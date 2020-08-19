'''
@Time    : 2020/2/29 21:21
@FileName: 235lowestCommonAncestor.py
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
    # 使用循环
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        a, b = sorted([p.val, q.val])
        while not a <= root.val <= b:
            if a > root.val:
                root = root.right
            else:
                root = root.left
        return root

    # 使用递归
    def lowestCommonAncestor1(self, root, p, q):
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

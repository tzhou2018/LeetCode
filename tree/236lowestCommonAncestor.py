'''
@Time    : 2020/2/29 21:46
@FileName: 236lowestCommonAncestor.py
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 在左子树中没有找到，那一定在右子树中
        if not left:
            return right
        # 在右子树中没有找到，那一定在右子树中
        elif not right:
            return left
        # 在左右子树中没有找到，那一定在右子树中
        else:
            return root


def test(root, p, q):
    if not root or root == p or root == q:
        return root
    left = test(root.left, p, q)
    right = test(root.right, p, q)
    if not left:
        return right
    elif not right:
        return left
    else:
        return root

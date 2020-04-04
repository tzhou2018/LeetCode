'''
@Time    : 2020/3/1 21:49
@FileName: 530getMinimumDifference.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 思路：
"""
利用二叉查找树的中序遍历为有序的性质，
计算中序遍历中临近的两个节点之差的绝对值，取最小值。
"""
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxInf = float('inf')
        self.preNone = None

        def minOrdBST(root):
            if not root:
                return None
            minOrdBST(root.left)
            if self.preNone:
                self.maxInf = min(self.maxInf, root.val - self.preNone.val)
            self.preNone = root
            minOrdBST(root.right)
        minOrdBST(root)
        return self.maxInf

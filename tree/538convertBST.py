'''
@Time    : 2020/2/27 22:17
@FileName: 538convertBST.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 先遍历右子树
class Solution(object):
    tem = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.convert(root)
        return root

    def convert(self, root):
        if not root:
            return None
        self.convert(root.right)
        self.tem += root.val
        root.val = self.tem
        self.convert(root.left)

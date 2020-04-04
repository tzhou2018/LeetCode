'''
@Time    : 2020/2/24 20:14
@FileName: 671findSecondMinimumValue.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        if not root.left and not root.right:
            return -1
        leftVal = root.left.val
        rightVal = root.right.val
        if leftVal == root.val:
            leftVal = self.findSecondMinimumValue(root.left)
        if rightVal == root.val:
            rightVal = self.findSecondMinimumValue(root.right)
        if leftVal != -1 and rightVal != -1:
            return min(leftVal, rightVal)
        if leftVal != -1:
            return leftVal
        return rightVal

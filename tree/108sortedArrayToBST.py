'''
@Time    : 2020/2/29 22:14
@FileName: 108sortedArrayToBST.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.toBST(nums, 0, len(nums) - 1)
        return root

    def toBST(self, nums, sInd, eInd):
        if sInd > eInd:
            return None
        mInd = (sInd + eInd) // 2
        node = TreeNode(nums[mInd])
        node.left = self.toBST(nums, sInd, mInd - 1)
        node.right = self.toBST(nums, mInd + 1, eInd)
        return node

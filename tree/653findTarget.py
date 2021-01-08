'''
@Time    : 2020/3/1 21:12
@FileName: 653findTarget.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 思路：
# 首先中序遍历二叉树， 将节点值存储到数组 nums 中
# 使用双指针遍历nums, 找到满足条件的值
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = []
        self.minOrdBST(root, nums)
        print(nums)
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] < k:
                start += 1
            elif nums[start] + nums[end] > k:
                end -= 1
            else:
                return True
        return False

    def minOrdBST(self, root, nums):
        if not root:
            return None
        self.minOrdBST(root.left, nums)
        nums.append(root.val)
        self.minOrdBST(root.right, nums)


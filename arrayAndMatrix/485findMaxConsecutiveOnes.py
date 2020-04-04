'''
@Time    : 2020/3/8 16:49
@FileName: 485findMaxConsecutiveOnes.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        res = 0
        for num in nums:
            cur = 0 if num == 0 else cur + 1
            res = max(res, cur)
        return res

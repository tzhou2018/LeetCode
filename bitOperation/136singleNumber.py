'''
@Time    : 2020/3/13 20:10
@FileName: 136singleNumber.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

# 两个相同的数异或的结果为 0，对所有数进行异或操作，最后的结果就是单独出现的那个数
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res

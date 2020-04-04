'''
@Time    : 2020/3/13 20:37
@FileName: 286missingNumber.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
两个相同的数异或一定是0的，因为这两个数的二进制完全相同。
第三点是异或是满足结合律的，因为一共n个数我们就把角标和该角标对应的值相互异或，
因为少一个数所以最后一定是少的那个数的角标异或0，可以看官方给出的这个图片

这里2就是确实缺失的数值，因为我们只能获取到角标2但是获取不到值为2的数字。最后就变成了0异或（缺少的的那个值），
"""


class Solution(object):
    # 方法1：
    # 使用异或运算
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res
    # 方法2：
    # 作差
    def missingNumber2(self, nums):
        return sum(range(len(nums) + 1)) - sum(nums)

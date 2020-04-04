'''
@Time    : 2020/3/20 10:40
@FileName: 169majorityElement.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    """
    # 方法1
    可以利用 Boyer-Moore Majority Vote Algorithm 来解决这个问题，
    使得时间复杂度为 O(N)。可以这么理解该算法：使用 cnt 来统计一个元素出现的次数，当遍历到的元素和统计元素不相等时
    ，令 cnt--。如果前面查找了 i 个元素，且 cnt == 0，说明前 i 个元素没有 majority，或者有 majority，
    但是出现的次数少于 i / 2，因为如果多于 i / 2 的话 cnt 就一定不会为 0。
    此时剩下的 n - i 个元素中，majority 的数目依然多于 (n - i) / 2，因此继续查找就能找出 majority。
    """

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        majority = nums[0]
        cnt = 0
        for num in nums:
            if cnt == 0:
                majority = num
            if majority == num:
                cnt += 1
            else:
                cnt -= 1
        return majority

    # 方法2
    # 首先对nums进行排序，出现频次大于数组长度一半的元素一定出现在中间位置
    def majorityElemen1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]

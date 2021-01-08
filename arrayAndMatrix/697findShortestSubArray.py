'''
@Time    : 2020/3/9 19:46
@FileName: 697findShortestSubArray.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
思路：
注意到，最短连续子数组的长度为多次出现的某个元素的最后索引减去第一次出现的索引，在加上1
定义三个dictionary，第一个用来统计每个元素出现的次数，
第二个用来统计元素第一次出现的索引，
第三个用来统计元素最后一次出现的索引
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsCnt = {}
        numsLastIndex = {}
        numsFristIndex = {}
        for i in range(len(nums)):
            numsCnt[nums[i]] = numsCnt.get(nums[i], 0) + 1
            numsLastIndex[nums[i]] = i
            if nums[i] not in numsFristIndex:
                numsFristIndex[nums[i]] = i
        maxCnt = 0
        for num in nums:
            maxCnt = max(maxCnt, numsCnt[num])
        ret = len(nums)
        for i in range(len(nums)):
            cnt = numsCnt[nums[i]]
            if cnt != maxCnt:
                continue
            ret = min(ret, numsLastIndex[nums[i]] - numsFristIndex[nums[i]] + 1)
        return ret


if __name__ == '__main__':
    print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))

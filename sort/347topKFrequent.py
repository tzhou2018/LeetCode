'''
@Time    : 2020/3/16 10:09
@FileName: 347topKFrequent.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
首先统计每个数出现的频次。
设置若干个桶，每个桶存储出现频率相同的数。桶的下标表示数出现的频率，
即第 i 个桶中存储的数出现的频率为 i。

把数都放到桶之后，从后向前遍历桶，最先得到的 k 个数就是出现频率最多的的 k 个数。
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequencyForNum = {}
        for num in nums:
            frequencyForNum[num] = frequencyForNum.get(num, 0) + 1
        buckets = [0] * (len(nums) + 1)
        for key, v in frequencyForNum.items():
            if buckets[v] == 0:
                buckets[v] = []
            buckets[v].append(key)
        topK = []
        for i in range(len(buckets) - 1, 0, -1):
            if len(topK) < k:
                if buckets[i] == 0:
                    continue
                if len(buckets[i]) <= k - len(topK):
                    topK.extend(buckets[i])
                else:
                    topK.extend(buckets[i][0:k - len(topK)])
            else:
                return topK
        return topK


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 1, 2, 2, 3, 4, 4, 4], 2))

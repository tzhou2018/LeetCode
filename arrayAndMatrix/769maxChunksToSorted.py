'''
@Time    : 2020/3/9 21:27
@FileName: 769maxChunksToSorted.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        res = 0
        right = arr[0]
        arrLen = len(arr)
        for i in range(arrLen):
            right = max(right, arr[i])
            if right == i:
                res += 1
        return res

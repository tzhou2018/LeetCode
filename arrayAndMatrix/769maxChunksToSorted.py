'''
@Time    : 2020/3/9 21:27
@FileName: 769maxChunksToSorted.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
首先找到从左块开始最小块的大小。如果前 k 个元素为 [0, 1, ..., k-1]，
可以直接把他们分为一个块。当我们需要检查 [0, 1, ..., n-1] 中
前 k+1 个元素是不是 [0, 1, ..., k] 的时候，只需要检查其中最大的数是不是 k 就可以了。

"""


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


if __name__ == '__main__':
    arr = [1, 3, 0, 2, 4]
    print(Solution().maxChunksToSorted(arr))

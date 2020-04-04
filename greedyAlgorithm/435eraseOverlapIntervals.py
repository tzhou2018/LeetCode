'''
@Time    : 2020/3/16 15:53
@FileName: 435eraseOverlapIntervals.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
先计算最多能组成的不重叠区间个数，然后用区间总个数减去不重叠区间的个数。

在每次选择中，区间的结尾最为重要，选择的区间结尾越小，留给后面的区间的空间越大，
那么后面能够选择的区间个数也就越大。

按区间的结尾进行排序，每次选择结尾最小，并且和前一个区间不重叠的区间。
统计不重叠的区间，返回结果为总区间长度-不重叠区间个数
"""
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda i: i[-1])
        cnt = 1
        end = intervals[0][1]
        for l in range(1, len(intervals)):
            if intervals[l][0] < end:
                continue
            cnt += 1
            end = intervals[l][1]
        return len(intervals) - cnt


if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))

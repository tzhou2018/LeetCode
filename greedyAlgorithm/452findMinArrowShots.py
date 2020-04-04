'''
@Time    : 2020/3/16 17:28
@FileName: 452findMinArrowShots.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 也是计算不重叠的区间个数，不过和435eraseOverlapIntervals 的区别
# 在于[1, 2] 和 [2, 3] 在本题中算是重叠区间。
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        points.sort(key=lambda i: i[-1])
        cnt = 1
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= end:
                continue
            cnt += 1
            end = points[i][1]
        return cnt

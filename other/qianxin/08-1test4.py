"""
@Time    : 2020/8/1 19:53
@FileName: 08-1test4.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""

import functools


class Lesson:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def maxK(o1, o2):
    return o1.end - o2.end


def startComaparator(o1, o2):
    return o1.start - o2.start


class Solution:
    def minUse(self):
        nLesson = int(input())
        res = 1
        lesssonArray = []
        for _ in range(nLesson):
            temp = list(map(int, input().strip().split(" ")))
            lesssonArray.append(Lesson(temp[0], temp[1]))
        lesssonArray = sorted(lesssonArray, key=functools.cmp_to_key(maxK))
        start = lesssonArray[0].start
        for i in range(1, nLesson):
            if lesssonArray[i].end == lesssonArray[i - 1].end:
                continue
            if start <= lesssonArray[i].start:
                res += 1
            start = lesssonArray[i].end
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.minUse())

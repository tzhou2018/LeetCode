"""
@Time    : 2020/8/1 20:12
@FileName: 08-1test05.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""

import functools


class Lesson:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def startComaparator(o1, o2):
    return o1.start - o2.start


class Solution:
    def minUse(self):
        nLesson = int(input())
        res = 0
        lesssonArray = []
        for _ in range(nLesson):
            temp = list(map(int, input().strip().split(" ")))
            lesssonArray.append(Lesson(temp[0], temp[1]))
        lesssonArray = sorted(lesssonArray, key=functools.cmp_to_key(startComaparator))
        end = lesssonArray[0].end
        for i in range(nLesson):
            if end < lesssonArray[i].end:
                res += 1
            end = lesssonArray[i].end
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.minUse())

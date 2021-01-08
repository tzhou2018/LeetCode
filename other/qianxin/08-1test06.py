"""
@Time    : 2020/8/1 20:18
@FileName: 08-1test06.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


class Solution:
    def minUse(self):
        nLesson = int(input())
        resList = []
        for _ in range(nLesson):
            temp = list(map(int, input().strip().split(" ")))
            resList.append(temp)

        return nLesson


if __name__ == '__main__':
    solution = Solution()
    print(solution.minUse())

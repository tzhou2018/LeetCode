'''
@Time    : 2020/2/14 20:27
@FileName: 70climbStairs.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        res = [0 for _ in range(n + 1)]
        res[1] = 1
        res[2] = 2
        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2]
        return res[n]


if __name__ == '__main__':
    print(Solution().climbStairs(8))

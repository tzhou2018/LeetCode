'''
@Time    : 2020/3/30 15:11
@FileName: 216combinationSum3.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def backTracking(curList, index):
            # recursion terminate
            if len(curList) == k and sum(curList) == n:
                res.append(curList)
                return
            # precess in current level
            # drill down
            for i in range(index, 10):
                backTracking(curList + [i], i + 1)

        backTracking([], 1)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum3(3, 7))

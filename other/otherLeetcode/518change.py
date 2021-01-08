"""
@Time    : 2020/7/27 22:02
@FileName: 518change.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.count = 0

        def change(candidates, target, index):
            if target < 0:
                return
            if target == 0:
                self.count += 1
            for i in range(index, len(candidates)):
                change(candidates, target - candidates[i], i)

        change(candidates, target, 0)
        return self.count


if __name__ == '__main__':
    print(Solution().combinationSum([1, 2, 3], 5))

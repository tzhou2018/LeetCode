'''
@Time    : 2020/3/30 10:43
@FileName: 39combinationSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def backTracking(candidates, target, currList, index):
            # recursion terminate
            if target < 0:
                return
            if target == 0:
                res.append(currList)
                return
                # precess logic in current level
            # drill down
            for i in range(index,len(candidates)):
                backTracking(candidates, target - candidates[i], currList + [candidates[i]], i)
                # reverse the level if needed

        backTracking(candidates, target, [], 0)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))

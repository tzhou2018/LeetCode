'''
@Time    : 2020/3/30 10:43
@FileName: 40combinationSum2.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        check = [0] * len(candidates)

        def backTracking(candidates, target, currList, index):
            # recursion terminate
            if target < 0:
                return
            if target == 0:
                res.append(currList)
                return
                # precess logic in current level
            # drill down
            for i in range(index, len(candidates)):
                if check[i] == 1:
                    continue
                if i > 0 and check[i] == 0 and candidates[i] == candidates[i - 1] and check[i - 1] == 0:
                    continue
                check[i] = 1
                backTracking(candidates, target - candidates[i], currList + [candidates[i]], i + 1)
                check[i] = 0
            # reverse the level if needed
            """
            处理方式2：
            for start in range(index, len(candidates)):
                # 去除重复的
                if previous != candidates[start]:
                    recursive(candidates, target - candidates[start], currList + [candidates[start]], start + 1)
                    previous = candidates[start]
            """

        backTracking(candidates, target, [], 0)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))

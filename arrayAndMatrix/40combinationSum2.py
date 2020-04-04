'''
@Time    : 2020/2/17 14:33
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
        result = []
        candidates.sort()

        def recursive(candidates, target, currList, index):
            if target < 0:
                return
            if target == 0:
                result.append(currList)
                return

            previous = -1
            for start in range(index, len(candidates)):
                # 去除重复的
                if previous != candidates[start]:
                    recursive(candidates, target - candidates[start], currList + [candidates[start]], start + 1)
                    previous = candidates[start]

        recursive(candidates, target, [], 0)
        return result


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

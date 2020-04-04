'''
@Time    : 2020/2/17 13:17
@FileName: 39combinationSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 用到递归，理解起来不太容易，使用栈图帮助理解
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []

        def recursive(candidates, target, curList, index):
            if target < 0:
                return
            if target == 0:
                result.append(curList)
                return
            for i in range(index, len(candidates)):
                recursive(candidates, target - candidates[i], curList + [candidates[i]], i)

        recursive(candidates, target, [], 0)
        return result


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))

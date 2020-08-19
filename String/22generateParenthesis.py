'''
@Time    : 2020/2/18 10:31
@FileName: 22generateParenthesis.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

# 回溯算法，深度优先遍历

"""
https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/
当前左右括号都有大于 0 0 个可以使用的时候，才产生分支；

产生左分支的时候，只看当前是否还有左括号可以使用；

产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支；

在当前的字符串长度等于 2 * n 时，满足要求，即，在左边和右边剩余的括号数都等于 0 0 的时候结算。

"""


class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backTracking(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backTracking(s + '(', left + 1, right)
            if right < left:
                backTracking(s + ')', left, right + 1)

        backTracking('', 0, 0)
        return result


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))

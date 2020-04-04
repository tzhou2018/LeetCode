'''
@Time    : 2020/3/17 16:08
@FileName: 241diffWaysToCompute.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
思路：
递归思想
可以通过运算符把整个式子分成两部分，两部分再利用递归解决。
以 2 * 3 - 4 * 5 为例。

2 和 3 - 4 * 5 两部分，中间是 * 号相连。

2 * 3 和 4 * 5 两部分，中间是 - 号相连。

2 * 3 - 4 和 5 两部分，中间是 * 号相连。

有了两部分的结果，然后再通过中间的符号两两计算加入到最终的结果中即可。
比如第一种情况，2 和 3 - 4 * 5 两部分，中间是 * 号相连。
2 的解就是 [2]，3 - 4 * 5 的解就是 [-5, -17]。
把两部分解通过 * 号计算，最终结果就是 [-10, -34]。
另外两种情况也类似。
然后还需要递归出口。
如果给定的字符串只有数字，没有运算符，那结果就是给定的字符串转为数字。

比如上边的第一种情况，2 的解就是 [2]。
作者：windliang
链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-5-5/
"""
from operator import *


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ops = {"+": add, "-": sub, "*": mul, "/": truediv}
        ans = []
        for i, c in enumerate(input):
            if c in ops:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for b in right:
                    for a in left:
                        ans.append(ops[c](a, b))
        return ans if ans else[int(input)]

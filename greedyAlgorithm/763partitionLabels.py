'''
@Time    : 2020/3/17 10:40
@FileName: 11partitionLabels.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
思路

策略就是不断地选择从最左边起最小的区间。可以从第一个字母开始分析，
假设第一个字母是 'a'，那么第一个区间一定包含最后一次出现的 'a'。
但第一个出现的 'a' 和最后一个出现的 'a' 之间可能还有其他字母，
这些字母会让区间变大。举个例子，在 "abccaddbeffe" 字符串中，
第一个最小的区间是 "abccaddb"。
通过以上的分析，我们可以得出一个算法：对于遇到的每一个字母，
去找这个字母最后一次出现的位置，用来更新当前的最小区间。

算法

定义数组 last[char] 来表示字符 char 最后一次出现的下标。
定义 left 和 right 来表示当前区间的首尾。如果遇到的字符最后一次出现的位置下标大于 right， 
就让 right=last[c] 来拓展当前的区间。当遍历到了当前区间的末尾时(即 i==right )，
把当前区间加入答案，同时将 left 设为 i+1 去找下一个区间。

作者：LeetCode
链接：https://leetcode-cn.com/problems/partition-labels/solution/hua-fen-zi-mu-qu-jian-by-leetcode/
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {e: i for i, e in enumerate(S)}
        left = right = 0
        res = []
        for i, e in enumerate(S):
            right = max(right, last[e])
            if right == i:
                res.append(right - left + 1)
                left = i + 1
        return res


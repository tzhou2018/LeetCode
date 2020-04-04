'''
@Time    : 2020/3/16 20:04
@FileName: 122maxProfit.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
对于 [a, b, c, d]，如果有 a <= b <= c <= d ，那么最大收益为 d - a。
而 d - a = (d - c) + (c - b) + (b - a) ，因此当访问到一个 prices[i] 且 
prices[i] - prices[i-1] > 0，那么就把 prices[i] - prices[i-1] 添加到收益中。
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
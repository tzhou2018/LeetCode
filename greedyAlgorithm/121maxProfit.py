'''
@Time    : 2020/3/16 19:45
@FileName: 121maxProfit.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
只要记录前面的最小价格，将这个最小价格作为买入价格，
然后将当前的价格作为售出价格，查看当前收益是不是最大收益。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lenPrices = len(prices)
        if lenPrices == 0:
            return 0
        maxP = 0
        minP = prices[0]
        for i in range(1, lenPrices):
            minP = min(minP, prices[i])
            maxP = max(maxP, prices[i] - minP)
        return maxP

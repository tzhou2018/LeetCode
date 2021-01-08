"""
@Time    : 2020/6/20 17:38
@FileName: 0611test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
"""
一道华为笔试题
    给一个数字n，统计出所有组合数和为n的数。
    思路： 使用递归解决
"""


# 参考：D:\Users\Solarzhou\PycharmProjects\TestCases\leetCode\arrayAndMatrix\39combinationSum.py
class Solution:
    res = 0

    def huawei01(self, n):
        # res = []
        self.recursive(n, 1, 0)
        return self.res

    def recursive(self, n, index, sum1):
        if sum1 > n:
            return
        if sum1 == n:
            # res.append()
            self.res += 1
            # return
        for i in range(index, n + 1):
            self.recursive(n, i, sum1 + i)


if __name__ == '__main__':
    print(Solution().huawei01(6))

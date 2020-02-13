'''
@Time    : 2020/2/9 20:45
@FileName: 06convert.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 思路
# 其实就是找规律，用一个数组存储三个字符，之后就是将字符追加到对应的三行中
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
        res, j, k = [''] * numRows, 0, 1
        for i in s:
            res[j] += i
            j += k
            if j == 0 or j == numRows - 1:
                k = -k
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().convert('AB', 1))

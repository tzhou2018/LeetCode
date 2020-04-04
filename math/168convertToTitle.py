'''
@Time    : 2020/3/18 21:25
@FileName: 168convertToTitle.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    # 递归
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        n -= 1
        return self.convertToTitle(n // 26) + chr(n % 26 + ord('A'))

    # 非递归
    def convertToTitle1(self, n):
        if n == 0:
            return ''
        res = ""
        while n:
            n, y = divmod(n, 26)  # 获得商和余数
            if y == 0:  # 如果余数为零，说明刚好整除，但是没有能获取到0对应的字母，所以需要从商借位给余数
                n -= 1
                y = 26
            res = chr(y + 64) + res  # 每循环一次，就给res左边加一个高位，之前的结果都在右边
        return res


if __name__ == '__main__':
    print(Solution().convertToTitle1(27))

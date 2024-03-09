'''
@Time    : 2020/2/9 21:37
@FileName: 08myAtoi.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0

        if str[0] == '+':
            result = self.convertS(str[1:])
        elif str[0] == '-':
            result = (-1) * self.convertS(str[1:])
        elif str[0] >= '0' and str[0] <= '9':
            result = self.convertS(str[:])
        else:
            return 0
        if result >= 2 ** 31 or result <= -2 ** 31:
            return 2 ** 31 - 1 if result > 0 else -2 ** 31
        return result

    def convertS(self, s):
        if not s:
            return 0
        res = 0
        for i in s:
            if i >= '0' and i <= '9':
                res = res * 10 + (ord(i) - ord('0'))
            else:
                return res
        return res


if __name__ == '__main__':
    print(Solution().myAtoi(" "))

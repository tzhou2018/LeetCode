'''
@Time    : 2020/3/18 16:23
@FileName: 504convertToBase7.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        isNegative = num < 0
        if isNegative:
            num = -num
        base7Str = []
        while num > 0:
            base7Str.append(str(num % 7))
            num = num // 7
        base7Str.reverse()
        return ''.join(base7Str) if not isNegative else '-' + ''.join(base7Str)


if __name__ == '__main__':
    print(Solution().convertToBase7(100))

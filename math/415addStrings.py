'''
@Time    : 2020/3/19 11:34
@FileName: 415addStrings.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) <= 0:
            return num2
        if len(num2) <= 0:
            return num1
        carry = 0
        res = ""
        num1Len = len(num1) - 1
        num2Len = len(num2) - 1
        while carry == 1 or num1Len >= 0 or num2Len >= 0:
            if num1Len >= 0:
                carry += int(num1[num1Len])
            if num2Len >= 0:
                carry += int(num2[num2Len])
            num1Len -= 1
            num2Len -= 1
            res += str(carry % 10)
            carry //= 10
        return res[::-1]
if __name__ == '__main__':
    print(Solution().addStrings('98','9'))

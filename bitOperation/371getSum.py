'''
@Time    : 2020/3/14 15:22
@FileName: 371getSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):

    def getSum(self, num1, num2):
        while num2 != 0:
            temp = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = temp & 0xffffffff
            num2 = carry
        return num1 if num1 >> 31 == 0 else num1 - 2 ** 32

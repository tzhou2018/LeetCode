'''
@Time    : 2020/3/19 10:32
@FileName: 67addBinary.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) <= 0:
            return b
        if len(b) <= 0:
            return a
        carry = 0
        aLen = len(a) - 1
        bLen = len(b) - 1
        c = ''
        while carry == 1 or aLen >= 0 or bLen >= 0:
            if aLen >= 0 and a[aLen] == '1':
                carry += 1
            if bLen >= 0 and b[bLen] == '1':
                carry += 1
            aLen -= 1
            bLen -= 1
            c += str(carry % 2)
            carry = carry // 2
        return c[:: -1]


if __name__ == '__main__':
    print(Solution().addBinary("1010", "1011"))

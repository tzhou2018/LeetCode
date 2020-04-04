'''
@Time    : 2020/3/14 14:32
@FileName: 476findComplement.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

# 思路：
# 对于 00000101，要求补码可以将它与 00000111 进行异或操作。
# 那么问题就转换为求掩码 00000111。
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 1
        res = 1 << 31
        while res & num == 0:
            res >>= 1
        return res << 1 ^ num

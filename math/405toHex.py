'''
@Time    : 2020/3/18 16:55
@FileName: 405toHex.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        mapHex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        res = ''
        if num == 0:
            return '0'
        num &= 0xFFFFFFFF
        while num > 0:
            res += (mapHex[num & 0b1111])
            num >>= 4
        return res[::-1] if res else '0'


if __name__ == '__main__':
    print(Solution().toHex(-1))

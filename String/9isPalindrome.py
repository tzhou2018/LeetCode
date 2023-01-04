"""
@Time    : 2020/3/5 9:40
@FileName: 9isPalindrome.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


# 思路1
# 将整数转化为字符串进行比较
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xList = list(str(x))
        start = 0
        end = len(xList) - 1
        while start < end:
            if xList[start] == xList[end]:
                start += 1
                end -= 1
                continue
            else:
                return False
        return True


# 思路2
# 将整数分为两部分进行比较;
# 取后一部分并进行反转；
# 回文长度是偶数或奇数；
def isPalindrome2(x):
    if x == 0:
        return True
    if x < 0 or x % 10 == 0:
        return False
    right = 0
    while x > right:
        right = right * 10 + x % 10
        x = x // 10
    return x == right or x == right // 10


if __name__ == '__main__':
    print(isPalindrome2(111))

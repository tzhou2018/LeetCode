'''
@Time    : 2020/2/10 19:38
@FileName: 09isPalindrome.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if len(str(x)) == 1:
            return True
        listX = list(str(x))
        start = 0
        end = len(listX) - 1
        while start < end:
            if listX[start] == listX[end]:
                start += 1
                end -= 1
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome(0))

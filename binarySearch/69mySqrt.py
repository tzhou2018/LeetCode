'''
@Time    : 2020/3/17 11:27
@FileName: 69mySqrt.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return False
        low = 1
        high = x
        while low <= high:
            mid = (low + high) // 2
            sqrt = mid * mid
            if sqrt > x:
                high = mid - 1
            elif sqrt < x:
                low = mid + 1
            else:
                return mid
        return high


if __name__ == '__main__':
    print(Solution().mySqrt(8))

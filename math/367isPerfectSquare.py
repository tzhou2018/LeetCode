'''
@Time    : 2020/3/20 10:56
@FileName: 367isPerfectSquare.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    # 方法1
    # 平方序列：1, 4, 9, 16,..
    # 间隔：3, 5, 7, ...
    # 间隔为等差数列，使用这个特性可以得到从1开始的平方序列。
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        subNum = 1
        while num > 0:
            num -= subNum
            subNum += 2
        return num == 0

    # 方法2
    # 二分法
    def isPerfectSquare1(self, num):
        if num < 2:
            return True
        left = 2
        right = num // 2
        while left <= right:
            mid = left + (right - left) // 2
            guessNum = mid * mid
            if guessNum == num:
                return True
            elif guessNum < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    print(Solution().isPerfectSquare1(2147483647))

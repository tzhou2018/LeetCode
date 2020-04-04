'''
@Time    : 2020/3/20 11:29
@FileName: 326isPowerOfThree.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n % 3 != 0:
                return False
            else:
                n //= 3
        return n == 1
    # 方法2
    # 整数限制
    # 参考链接：https://leetcode-cn.com/problems/power-of-three/solution/3de-mi-by-leetcode/
    def isPowerOfThree1(self, n):
        if n > 0:
            return (1162261467 % n) == 0
        else:
            return False

if __name__ == '__main__':
    print(Solution().isPowerOfThree(7))
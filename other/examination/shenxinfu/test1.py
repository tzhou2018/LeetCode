'''
@Time    : 2020/4/22 16:20
@FileName: test1.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
import sys


class Solution:
    def is_product(self, num):
        # write code here
        if num < 2:
            # print(0)
            return 0
        sum = 0
        i2, i5, i7 = 0, 0, 0
        ans = [1]
        while sum < num:
            num2, num5, num7 = ans[i2] * 2, ans[i5] * 5, ans[i7] * 7
            tmp = min(num2, num5, num7)
            if tmp == num2:
                i2 += 1
            if tmp == num5:
                i5 += 1
            if tmp == num7:
                i7 += 1
            ans.append(tmp)
            sum = ans[-1]
            if (sum == num):
                # print(1)
                return 1
        return 0


if __name__ == '__main__':
    num = int(sys.stdin.readline().strip())

    print(Solution().is_product(num))

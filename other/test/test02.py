'''
@Time    : 2020/4/29 11:13
@FileName: 08-08test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
一些常用的库函数
"""
# 传入比较器，进行排序，在python3 中去掉了cmp(x,y)
# 可以用functools.cmp_to_key()
import functools


class Solution:
    # 定义一个比较器
    def comparator(self, a, b):
        if a + b > b + a:
            return 1
        else:
            return -1

    def lowestString(self, strs):
        strs1 = sorted(strs, key=functools.cmp_to_key(solution.comparator))
        print(''.join(strs1))


    """
    class Solution1:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = list(map(str, numbers))
        len_num = len(numbers)
        # 每次循环确定一个元素
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len_num):
                tmp = int(numbers[i] + numbers[j]) - int(numbers[j] + numbers[i])
                if tmp > 0:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return ''.join(numbers)
    """

    def lowestString1(self, strs):
        strsLen = len(strs)
        for i in range(strsLen):
            for j in range(i + 1, strsLen):
                if strs[i] + strs[j] > strs[j] + strs[i]:
                    strs[i], strs[j] = strs[j], strs[i]
        return ''.join(strs)


if __name__ == '__main__':
    strs1 = ["jibw", "ji", "jp", "bw", "jibw"]
    solution = Solution()
    # solution.lowestString(strs1)
    print(solution.lowestString(strs1))

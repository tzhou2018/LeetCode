'''
@Time    : 2020/2/13 19:31
@FileName: test.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
import itertools


class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return ss
        result = []
        # 通俗地讲，就是返回可迭代对象的所有数学全排列方式
        k = itertools.permutations(ss)
        for i in k:
            print(i)
            result.append(''.join(i))
        result = list(set(result))
        result.sort()
        return result


if __name__ == '__main__':
    print(Solution().Permutation("ab"))

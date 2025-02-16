'''
@Time    : 2020/3/4 11:08
@FileName: 739dailyTemperatures.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 使用栈存储温度数组中的下标；
# 遍历数组，若是当前元素大于栈顶元素；
# 说明栈顶元素的下一个比它大的数就是当前元素。
# [1,1,1,2,1,4]
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        indexs = []
        res = [0 for _ in range(len(T))]
        for i in range(len(T)):
            while indexs and T[i] > T[indexs[-1]]:
                preindex = indexs.pop()
                res[preindex] = (i - preindex)
            indexs.append(i)
        return res


if __name__ == '__main__':
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

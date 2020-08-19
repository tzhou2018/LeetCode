'''
@Time    : 2020/3/22 19:40
@FileName: arrayFindValue.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 时间复杂度O(n2)， 运行超时
class Solution:
    def arrayFindValue(self, array):
        # write code here

        lenArray = len(array)
        res = []
        for i in range(lenArray - 1, 0, -1):
            cnt = 0
            for j in range(i - 1, -1, -1):
                if array[j] > array[i]:
                    cnt += 1
                if cnt > 1:
                    break
            if cnt == 1:
                res.append(i)
        if not res:
            res.append(-1)
        return res[::-1]

    # 保存当前所遍历的最大值，次大值 时间复杂度O(n)
    def arrayFindValue1(self, array):
        res = []
        max1 = array[0]
        max2 = float('inf')
        lenArray = len(array)
        for i in range(1, lenArray):
            if array[i] >= max1:
                max2 = max1
                max1 = array[i]
            elif array[i] >= max2:
                res.append(i)
                max2 = array[i]
        if not res:
            return res.append(-1)
        else:
            return res


if __name__ == '__main__':
    # array = input()
    # array = list(map(int, array.split()))
    array = [1, 22, 22, 33, 22, 12, 45, 44, 5]
    # print(Solution().arrayFindValue(array))
    res = Solution().arrayFindValue1(array)
    for v in res:
        print(v, end=' ')

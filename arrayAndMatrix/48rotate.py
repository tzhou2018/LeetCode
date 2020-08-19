'''
@Time    : 2020/2/17 15:00
@FileName: 48rotate.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 思路：
# 首先将原数组 第一列 与 最后一列互换，第二列与倒数第二列互换 ......
# 之后将相应对角元素互换

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        h = len(matrix)
        w = len(matrix[0])
        for i in range(0, h):
            for j in range(0, w // 2):
                matrix[i][j], matrix[i][w - j - 1] = matrix[i][w - j - 1], matrix[i][j]

        for i in range(0, h):
            for j in range(0, w - 1 - i):
                matrix[i][j], matrix[w - 1 - j][h - 1 - i] = matrix[w - 1 - j][h - 1 - i], matrix[i][j]


# 方法2
# 参考程序员面试指南解法
class Solution2:
    @staticmethod
    def roate(matrix):
        if not matrix or len(matrix) != len(matrix[0]):
            return None
        rows = len(matrix)
        cols = len(matrix[0])
        ur, uc = 0, 0
        dr, dc = rows - 1, cols - 1
        while ur < dr and uc < dc:
            Solution2.adjust(matrix, ur, uc, dr, dc)
            ur += 1
            uc += 1
            dc -= 1
            dr -= 1

    @staticmethod
    def adjust(arr, ur, uc, dr, dc):
        times = dc - uc
        for i in range(times):
            tempC = uc
            tempR = ur + i
            tempV = arr[tempR][tempC]
            arr[ur + i][uc] = arr[dr][uc + i]
            arr[dr][uc + i] = arr[dr - i][dc]
            arr[dr - i][dc] = arr[ur][dc - i]
            arr[ur][dc - i] = tempV


if __name__ == '__main__':
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    solution.rotate(arr)
    print(arr)
    # 方法2
    arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution2.roate(arr1)
    print(arr1)

'''
@Time    : 2020/3/8 17:17
@FileName: 240searchMatrix.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows = len(matrix) -1
        cols = len(matrix[0]) -1
        row, col = rows, 0
        while row >= 0 and col <= cols:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False

if __name__ == '__main__':
    array = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    print(Solution().searchMatrix(array, 56))

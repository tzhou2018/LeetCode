'''
@Time    : 2020/2/17 16:05
@FileName: 54spiralOrder.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
# 最好用的方法，见方法3

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        while matrix:
            ans += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return ans

    def turn(self, matrix):
        return list(map(list, zip(*matrix)))[::-1]


if __name__ == '__main__':
    print(Solution().spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))

# 方法 2
# 思路：
# 采用最原始的方法，循环打印；打印一圈分为四步：
# 1)从左至右；2）从上至下；3）从右至左；4）从下至上；

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        start = 0
        while (cols > start * 2 and rows > start * 2):
            ans = []
            result.extend(self.printMatrixCircle(ans, matrix, cols, rows, start))
            start += 1
        return result

    def printMatrixCircle(self, ans, matrix, cols, rows, start):
        endX = cols - 1 - start
        # print(endX)
        endY = rows - 1 - start
        for i in range(start, endX + 1):
            ans.append(matrix[start][i])
        if start < endY:
            for i in range(start + 1, endY + 1):
                ans.append(matrix[i][endX])
        if start < endX and start < endY:
            for i in range(endX - 1, start - 1, -1):
                ans.append(matrix[endY][i])
        if start < endX and start < endY:
            for i in range(endY - 1, start, -1):
                ans.append(matrix[i][start])
        return ans

# 方法3
# 参见《程序员面试指南》提供的方法--转圈打印，
# 与解法题48号类似

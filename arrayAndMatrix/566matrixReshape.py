'''
@Time    : 2020/3/8 16:31
@FileName: 566matrixReshape.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        res = [[0 for _ in range(c)] for _ in range(r)]
        index = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = nums[index // n][index % n]
                index += 1
        return res


if __name__ == '__main__':
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().matrixReshape(arr, 4, 3))

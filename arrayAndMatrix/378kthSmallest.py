'''
@Time    : 2020/3/8 19:33
@FileName: 378kthSmallest.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

# 二分查找
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        low, high = matrix[0][0], matrix[rows - 1][cols - 1]
        while low <= high:
            mid = low + (high - low) // 2
            count = 0
            for i in range(rows):
                for j in range(cols):
                    if matrix[i][j] <= mid:
                        count += 1
            if count < k:
                low = mid + 1
            else:
                high = mid - 1
        return low

# 使用堆

import heapq


class Solution(object):
  def kthSmallest(self, matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    visited = {(0, 0)}
    heap = [(matrix[0][0], (0, 0))]

    while heap:
      val, (i, j) = heapq.heappop(heap)
      k -= 1
      if k == 0:
        return val
      if i + 1 < len(matrix) and (i + 1, j) not in visited:
        heapq.heappush(heap, (matrix[i + 1][j], (i + 1, j)))
        visited.add((i + 1, j))
      if j + 1 < len(matrix) and (i, j + 1) not in visited:
        heapq.heappush(heap, (matrix[i][j + 1], (i, j + 1)))
        visited.add((i, j + 1))

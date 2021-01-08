"""
@Time       : 2020/9/5 9:49
@FileName   : 1004longestOnes.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right, count = 0, 0, 0
        for right in range(len(A)):
            if A[right] == 0:
                count += 1
            if count > K:
                if A[left] == 0:
                    count -= 1
                left += 1
        return right - left + 1

"""
@Time:  2023/7/14 23:50
@FileName:  bubbleSort.py
@Author:    zhoutong
@Email:
@Describe:
"""

#  java
# int [] arr = {1,2,3}
# O(n**2)
# big O(n**2)
# [1,2,3,4]

arr = [4, 3, 2, 1]


# len(arr)
# 一次比较

# arr = [3,2,1,4,]


def bubbleSort(arr):
    for i in range(1, len(arr)):  # n 次
        for j in range(0, len(arr) - i):  # n-1; n-2; n-3; n-4
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



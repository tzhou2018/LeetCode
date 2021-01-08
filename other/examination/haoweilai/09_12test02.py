"""
@Time       : 2020/9/12 13:53
@FileName   : 09_12test02.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""

import random


def test02():
    n = int(input())
    arr = list(map(int, input().strip().split(" ")[:n]))
    # print(arr)
    arr.sort(reverse=True)
    # arr = heapSort(arr)
    # quickSort(arr, 0, len(arr) - 1)
    for e in arr:
        print(e, end=" ")


# 快排
# def quickSort(arr, lo, hi):
#     if lo < hi:
#         # swap(arr, lo + int(random.random() * (hi - lo)), lo)
#         piviot = partition(arr, lo, hi)
#         quickSort(arr, lo, piviot - 1)
#         quickSort(arr, piviot + 1, hi)
#
#
# def partition(arr, lo, hi):
#     i = lo
#     while lo < hi:
#         while lo < hi and arr[i] <= arr[hi]:
#             hi -= 1
#         while lo < hi and arr[i] >= arr[lo]:
#             lo += 1
#
#         swap(arr, lo, hi)
#     swap(arr, i, hi)
#     return hi

# 使用堆排，降低空间复杂度
# def heapSort(arr):
#     if not arr or len(arr) < 2:
#         return arr
#     for i in range(len(arr)):
#         heapInsert(arr, i)
#     heapSize = len(arr) - 1
#     swap(arr, 0, heapSize)
#     while heapSize > 0:
#         heapify(arr, 0, heapSize)
#         heapSize -= 1
#         swap(arr, 0, heapSize)
#     return arr
#
#
# def heapInsert(arr, index):
#     while (arr[index] > arr[int((index - 1) / 2)]):
#         swap(arr, index, int((index - 1) / 2))
#         index = int((index - 1) / 2)
#
#
# def heapify(arr, index, heapSize):
#     left = index * 2 + 1
#     while left < heapSize:
#         largest = left + 1 if left + 1 < heapSize and arr[left + 1] > arr[left] else left
#         largest = largest if arr[largest] > arr[index] else index
#         if index == largest:
#             break
#         swap(arr, largest, index)
#         index = largest
#         left = index * 2 + 1
#
#
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    test02()

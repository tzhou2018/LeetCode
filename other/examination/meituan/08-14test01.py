"""
@Time    : 2020/8/14 10:50
@FileName: 08-14test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


# 写一个堆排序
def heapSort(arr):
    for i in range(len(arr)):
        heapInsert(arr, i)
    heapSize = len(arr) - 1
    swap(arr, 0, heapSize)
    while heapSize > 0:
        heapSize -= 1
        heapify(arr, 0, heapSize)
        heapSize -= 1
        swap(arr, 0, heapSize)
    return arr


def heapInsert(arr, index):
    while arr[index] > arr[(index - 1) // 2]:
        swap(arr, index, (index - 1) // 2)
        index = (index - 1) // 2
        pass


def heapify(arr, index, heapSize):
    left = index * 2 + 1
    while left < heapSize:
        largest = left + 1 if left + 1 < heapSize and arr[left + 1] > arr[left] else left
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        swap(arr, index, largest)
        left = index * 2 + 1


def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]


import random


def quickSort(arr, lo, hi):
    if hi > lo:
        swap(arr, hi, lo + int(random.random() * (hi - lo + 1)))
        pivot = partition(arr, 0, len(arr) - 1)
        quickSort(arr, lo, pivot[0] - 1)
        quickSort(arr, pivot[1] + 1, hi)
    return arr
    pass


def partition(arr, lo, hi):
    less = lo - 1
    most = hi
    while lo < most:
        if arr[lo] < arr[hi]:
            less += 1
            swap(arr, less, lo)
            lo += 1
        elif arr[lo] > arr[hi]:
            most -= 1
            swap(arr, lo, most)
        else:
            lo += 1
    swap(arr, most, hi)
    return [less + 1, most]

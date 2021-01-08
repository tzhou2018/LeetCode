"""
@Time    : 2020/8/22 10:28
@FileName: 08-22test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
# 3 /2 = 1.5
# 1
# arr
# i 0  v 3
# i 1  v 1
"""
[15,12]
    15
12
---------------
    12
15
[12,15]
------------------
[12,15,10]

    12
15      10

[10,15,12]

"""


def heapSort(arr):
    print(arr)
    for i in range(len(arr)):
        heapInsert(arr, i)
    print(arr, "jius")
    heapSize = len(arr)
    heapSize -= 1
    swap(arr, 0, heapSize)
    while heapSize > 0:
        heapAjust(arr, 0, heapSize)
        heapSize -= 1
        swap(arr, 0, heapSize)
    print(arr)


def heapInsert(arr, index):
    while arr[int((index - 1) / 2)] > arr[index]:
        swap(arr, int((index - 1) / 2), index)
        index = int((index - 1) / 2)


def heapInsert1(arr, index):
    while (arr[index] > arr[int((index - 1) / 2)]):
        swap(arr, index, int((index - 1) / 2))
        index = int((index - 1) / 2)


def heapAjust(arr, index, heapSize):
    left = index * 2 + 1
    while left < heapSize:
        smaller = left + 1 if left + 1 < heapSize and arr[left + 1] < arr[left] else left
        smaller = index if arr[smaller] > arr[index] else smaller
        if smaller == index:
            break
        swap(arr, index, smaller)
        index = left
        left = index * 2 + 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = [3, 1, 4, 5, 2]
    heapSort(arr)

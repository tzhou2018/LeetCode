'''
@Time    : 2020/4/5 11:20
@FileName: heapSort.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


def heapSort(array):
    arrayLen = len(array) - 1
    for i in range(arrayLen // 2, -1, -1):
        heapAjust(array, i, arrayLen)
    for i in range(arrayLen, 0, -1):
        # 将堆顶记录和当前未经排序子序列的最后一个记录交换
        swap(array, 0, i)
        # 将array[0:i-1]重新调整为大顶堆
        heapAjust(array, 0, i - 1)
    return array


def heapAjust(array, s, m):
    # temp 记录当前值，也就是非终端节点值
    temp = array[s]
    j = s * 2 + 1
    while j <= m:
        if j < m and array[j] < array[j + 1]:
            j += 1
        if temp >= array[j]:
            break
        array[s] = array[j]
        s = j
        j *= 2
    # array[s] 为根节点的值
    array[s] = temp


def swap(array, first, i):
    array[first], array[i] = array[i], array[first]


# 另一种写法,更清爽
def heapSort1(arr):
    if not arr or len(arr) < 2:
        return 0
    for i in range(len(arr)):
        heapInsert(arr, i)
    heapSize = len(arr) - 1
    swap(arr, 0, heapSize)
    while (heapSize > 0):
        heapify(arr, 0, heapSize)
        heapSize -= 1
        swap(arr, 0, heapSize)
    return arr


def heapInsert(arr, index):
    while (arr[index] > arr[int((index - 1) / 2)]):
        swap(arr, index, int((index - 1) / 2))
        index = int((index - 1) / 2)


def heapify(arr, index, heapSize):
    left = index * 2 + 1
    while left < heapSize:
        largest = left + 1 if left + 1 < heapSize and arr[left + 1] > arr[left] else left
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        swap(arr, largest, index)
        index = largest
        left = index * 2 + 1


# python 内置堆函数
import heapq


def innerHeap(str):
    heapq.heapify(str)
    res = []
    while str:
        res.append(heapq.heappop(str))
    return res


if __name__ == '__main__':
    array = [50, 10, 90, 30, 40, 0, 80, 70, 60, 80]
    print(heapSort1(array[:]))
    # print(array)
    # print(innerHeap(array))

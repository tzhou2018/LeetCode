# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/6/6 20:17
desc:
'''
import functools


class Node:
    def __init__(self, d, m, users):
        self.d = d
        self.m = m
        self.users = users


# 比较器
def minDiskComparator(o1, o2):
    return o1.d - o2.d


def minMemoryComparator(o1, o2):
    return o1.m - o2.m


def maxUsersCompatator(o1, o2):
    return o2.users - o1.users


def mostUser():
    input1 = input().strip().split(" ")
    disk = int(input1[0])
    memory = int(input1[1])
    appList = input1[2].split("#")
    nodes = []
    res1 = 0
    res2 = 0
    userHeap = []
    for i in range(len(appList)):
        app = appList[i].split(",")
        nodes.append(Node(int(app[0]), int(app[1]), int(app[2])))
    diskHeap = sorted(nodes, key=functools.cmp_to_key(minDiskComparator))
    # heapq.heapify(diskHeap)
    while diskHeap and diskHeap[0].m <= memory and diskHeap[0].d <= disk:
        node = diskHeap.pop(0)
        userHeap.append(node)
    userHeap = sorted(userHeap, key=functools.cmp_to_key(maxUsersCompatator))
    while userHeap and disk >= userHeap[0].d and memory >= userHeap[0].m:
        node = userHeap.pop(0)
        res1 += node.users
        disk -= node.d
        memory -= node.m
    # 根据 memory 大小排序计算users
    disk = int(input1[0])
    memory = int(input1[1])
    userHeap.clear()
    memoryHeap = sorted(nodes, key=functools.cmp_to_key(minMemoryComparator))
    while memoryHeap and memoryHeap[0].m <= memory and memoryHeap[0].d <= disk:
        node = memoryHeap.pop(0)
        userHeap.append(node)
    userHeap = sorted(userHeap, key=functools.cmp_to_key(maxUsersCompatator))
    while userHeap and disk >= userHeap[0].d and memory >= userHeap[0].m:
        node = userHeap.pop(0)
        res2 += node.users
        disk -= node.d
        memory -= node.m
    return max(res2, res1)


if __name__ == '__main__':
    print(mostUser())

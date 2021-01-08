"""
@Time    : 2020/8/1 16:08
@FileName: 08-1-08-08test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
import functools


class Node:
    def __init__(self, Pn, Wn):
        self.Pn = Pn
        self.Wn = Wn


class Solution:
    def minPnComparator(self, o1, o2):
        return o1.Pn - o2.Pn

    def maxWnComparator(self, o1, o2):
        return o2.Wn - o1.Wn

    def mostWn(self):
        allT = int(input())
        itemN = int(input())
        nodes = []
        WnHeap = []
        res = 0
        for _ in range(itemN):
            temp = list(map(int, input().strip().split(" ")))
            nodes.append(Node(temp[0], temp[1]))
        PnHeap = sorted(nodes, key=functools.cmp_to_key(self.minPnComparator))
        while PnHeap and PnHeap[0].Pn < allT:
            node = PnHeap.pop(0)
            WnHeap.append(node)
        WnHeap = sorted(WnHeap, key=functools.cmp_to_key(self.maxWnComparator))
        while WnHeap and allT > 0:
            node = WnHeap.pop(0)
            if allT >= node.Wn:
                res += node.Wn
                allT -= node.Pn
        return res


"""
79 83
58 81
86 54
110 150
62 52
45 48
68 62
30 22
"""
if __name__ == '__main__':
    res = Solution()
    print(res.mostWn())

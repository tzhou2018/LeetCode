"""
@Time    : 2020/8/1 16:08
@FileName: 08-1-08-08test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
import functools


class Node:
    def __init__(self, Pn, Wn, PW):
        self.Pn = Pn
        self.Wn = Wn
        self.PW = PW


class Solution:
    def minPnComparator(self, o1, o2):
        return o1.Pn - o2.Pn

    def maxWnComparator(self, o1, o2):
        return o2.Wn - o1.Wn

    def maxPWcomparator(self, o1, o2):
        return o2.PW - o1.PW

    def mostWn(self):
        allT = int(input())
        allT2 = allT
        itemN = int(input())
        nodes = []
        WnHeap = []
        PWHeap = []
        res1 = 0
        res2 = 0
        for _ in range(itemN):
            temp = list(map(int, input().strip().split(" ")))
            nodes.append(Node(temp[0], temp[1], (temp[1] - temp[0])))

        PnHeap = sorted(nodes, key=functools.cmp_to_key(self.minPnComparator))
        while PnHeap and PnHeap[0].Pn < allT:
            node = PnHeap.pop(0)
            WnHeap.append(node)

        WnHeap = sorted(WnHeap, key=functools.cmp_to_key(self.maxWnComparator))
        while WnHeap and allT > 0:
            node = WnHeap.pop(0)
            if allT >= node.Wn:
                res1 += node.Wn
                allT -= node.Pn
        # 同上面的方法
        # 按照性价比进行一次计算
        PnHeap.clear()
        PnHeap = sorted(nodes, key=functools.cmp_to_key(self.minPnComparator))
        while PnHeap and PnHeap[0].Pn < allT2:
            node = PnHeap.pop(0)
            PWHeap.append(node)
        PWHeap = sorted(PWHeap, key=functools.cmp_to_key(self.maxPWcomparator))
        while PWHeap and allT2 > 0:
            node = PWHeap.pop(0)
            if allT2 >= node.Wn:
                print(node.Wn)
                res2 += node.Wn
                allT2 -= node.Pn
        return max(res1, res2)


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

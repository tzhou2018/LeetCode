'''
@Time    : 2020/4/26 20:10
@FileName: quence.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

import sys


class Solution:
    def __init__(self):
        self.arr = []

    def fun1(self):
        # arr = []
        # res = []
        T = int(sys.stdin.readline().strip())
        if T < 1 or T > 100:
            return 0
        for i in range(T):
            Q = int(sys.stdin.readline().strip())
            if Q < 1 or Q > 1000:
                return 0
            for _ in range(Q):
                input1 = sys.stdin.readline().strip().split()
                e0 = input1[0]
                # e1 = input1[1]
                if e0 == "PUSH":
                    e1 = int(input1[1])
                    if e1 < 1 or e1 > 1000:
                        return 0
                    self.pushQ(int(input1[1]))
                elif e0 == "TOP":
                    v = self.topQ()
                    if v == -1:
                        print(str(v))
                    print(v)
                    # res.append(v)
                elif e0 == "POP":
                    v = self.popQ()
                    if v == -1:
                        print(str(v))
                        # res.append(v)
                elif e0 == "SIZE":
                    size = self.sizeQ()
                    print(size)
                    # res.append(size)
                elif e0 == "CLEAR":
                    self.clearQ()
                else:
                    print(0)

    def pushQ(self, v):
        self.arr.append(v)

    def topQ(self):
        if not self.arr:
            return -1
        return self.arr[0]

    def popQ(self):
        if not self.arr:
            return -1
        else:
            return self.arr.pop(0)

    def sizeQ(self):
        return len(self.arr)

    def clearQ(self):
        self.arr.clear()


if __name__ == '__main__':
    Solution().fun1()

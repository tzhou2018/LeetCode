'''
@Time    : 2020/3/3 20:58
@FileName: 232twoStackToQuence.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

import sys


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def fun1(self):
        n = int(sys.stdin.readline().strip())
        for _ in range(n):
            input1 = sys.stdin.readline().split()
            e0 = input1[0]
            if e0 == "add":
                self.push(int(input1[1]))
            elif e0 == "poll":
                self.pop()
            elif e0 == "peek":
                val = self.peek()
                print(val)

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


if __name__ == '__main__':
    MyQueue().fun1()

# 使用一个辅助栈 minData, 辅助栈的长度始终与栈 data 保持一致；
# 当且栈顶存储当前栈中的最小值
class MinStack:
    def __init__(self):
        self.data = []
        self.minStack = []
        self.val = float('inf')

    def push(self, node):
        self.data.append(node)
        self.val = min(node, self.val)
        self.minStack.append(self.val)

    def pop(self):
        self.data.pop()
        self.minStack.pop()
        self.val = self.minStack[-1] if self.minStack else float('inf')

    def top(self):
        return self.data[-1]

    def getMin(self):
        if not self.minStack:
            return None
        else:
            return self.minStack[-1]

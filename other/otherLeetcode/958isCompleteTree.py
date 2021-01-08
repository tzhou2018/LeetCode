"""
@Time    : 2020/8/1 11:34
@FileName: 958isCompleteTree.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
import collections

# 思路：层次遍历
# 若当前节点已进入到叶子节点判断，则左节点或右节点有一个不为空时就返回False
# 当前未进入到叶子结点判断，则左节点不为空，右节点为空时返回False
class Solution:
    def isCompleteTree(self, root):
        if not root:
            return True
        queue = collections.deque()
        queue.append(root)
        leaf = False
        while queue:
            node = queue.popleft()
            left = node.left
            right = node.right
            if (leaf and (left or right)) or (left and not right):
                return False
            if left:
                queue.append(left)
            if right:
                queue.append(right)
            else:
                leaf = True
        return True

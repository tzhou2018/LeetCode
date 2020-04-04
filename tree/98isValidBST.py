'''
@Time    : 2020/3/29 14:07
@FileName: 98isValidBST.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 中顺遍历，遍历时比较当前结点与下一个结点的大小
class Solution(object):
    last = float('-inf')
    flag = True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if self.flag:
            self.isValidBST(root.left)
        if root.val <= self.last:
            self.flag = False
        self.last = root.val
        if self.flag:
            self.isValidBST(root.right)
        return self.flag


def listCreatTree(root, llist, i):
    if i < len(llist):
        if llist[i] == '#':
            return None  ###这里的return很重要
        else:
            root = TreeNode(llist[i])
            # 往左递推
            root.left = listCreatTree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listCreatTree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  ###这里的return很重要
    return root


if __name__ == '__main__':
    root = listCreatTree(None, [1, 1], 0)
    print(Solution().isValidBST(root))

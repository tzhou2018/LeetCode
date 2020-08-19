'''
@Time    : 2020/2/27 21:47
@FileName: 230kthSmallest.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = []

    # 中序遍历便可找到满足要求的数
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.midOrdBT(root)
        return self.res[k - 1]

    def midOrdBT(self, root):
        if not root:
            return '#'
        self.midOrdBT(root.left)
        self.res.append(root.val)
        self.midOrdBT(root.right)


# 另一种写法
class Solution2:
    def kthSmallest(self, root, k):
        if not root or k < 1:
            return None
        stack = []
        count = 0
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                count += 1
                if count == k:
                    return root.val
                root = root.right


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
    llist = [4, 2, 6, '#', 3, 5, 7]
    root = listCreatTree(None, llist, 0)
    print(Solution().kthSmallest(root, 2))
    print(Solution2().kthSmallest(root, 2))

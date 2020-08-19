'''
@Time    : 2020/2/21 20:40
@FileName: 617mergeTrees.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return 0
        if not t1:
            return 0
        if not t2:
            return 0
        # class Solution(object):
        #     def mergeTrees(self, t1, t2):
        #         """
        #         :type t1: TreeNode
        #         :type t2: TreeNode
        #         :rtype: TreeNode
        #         """
        #         if t1 or t2:
        #             root = TreeNode((t1 and t1.val or 0) + (t2 and t2.val or 0))
        #             root.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        #             root.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        #             return root

        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root


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


def preOrderBT(root):
    if not root:
        return None
    print(root.val, end='\t')
    preOrderBT(root.left)
    preOrderBT(root.right)


if __name__ == '__main__':
    llist1 = [1, 3, 2, 5]
    t1 = listCreatTree(None, llist1, 0)
    preOrderBT(t1)
    # llist2 = [2, 1, 3, '#', 4, 7]
    llist2 = [1, 3, 2, 5]
    t2 = listCreatTree(None, llist2, 0)
    root = Solution().mergeTrees(t1, t2)
    print()
    # print(root.right.val)
    preOrderBT(root)

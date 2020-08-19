'''
@Time    : 2020/2/22 21:29
@FileName: 437pathSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        count = self.pathSumStartWithRoot(root, sum) + self.pathSum(root and root.left or None, sum) + \
                self.pathSum(root and root.right or None, sum)
        return count

    def pathSumStartWithRoot(self, root, num):
        if not root:
            return 0
        count = 0
        if root.val == num:
            count += 1
        count += self.pathSumStartWithRoot(root.left, num - root.val) + \
                 self.pathSumStartWithRoot(root.right, num - root.val)

        return count


# 另一种写法
class Solution2:
    def pathSum(self, root, num):
        if not root:
            return 0
        # count = pathSumStartWithRoot(root, num) + pathSum(root and root.left or None, num) + \
        #         pathSum(root and root.right or None, num)
        count = self.pathSumStartWithRoot(root, num) + self.pathSum(root.left, num) + \
                self.pathSum(root.right, num)
        return count

    def pathSumStartWithRoot(self, root, num):
        if not root:
            return 0
        stack = [(root, [root.val])]
        count = 0
        while stack:
            node, path = stack.pop()
            if sum(path) == num:
                count += 1
            if node.left:
                stack.append((node.left, path + [node.left.val]))
            if node.right:
                stack.append((node.right, path + [node.right.val]))
        return count


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
    llist = [1, 2, 3, '#', 4, 5, 6]
    root = listCreatTree(None, llist, 0)
    print(Solution().pathSum(root, 6))
    print(Solution2().pathSum(root, 6))

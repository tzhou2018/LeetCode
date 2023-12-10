'''
@Time    : 2020/2/26 21:36
@FileName: 513findBottomLeftValue.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        res = []
        curLayerNode = []
        curLayerNode.append(root)
        res.append([root])
        while curLayerNode:
            nextLayerNode = []
            while curLayerNode:
                node = curLayerNode.pop(0)
                if node.left:
                    nextLayerNode.append(node.left)
                if node.right:
                    nextLayerNode.append(node.right)
            # 进行一次判断，若下层为空，则该层是最后一层
            if nextLayerNode:
                res.append(nextLayerNode[:])
            curLayerNode = nextLayerNode
        return res[-1][0].val


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


# def preOrderBT(root):
#     if not root:
#         return None
#     print(root.val, end='\t')
#     preOrderBT(root.left)
#     preOrderBT(root.right)


if __name__ == '__main__':
    llist = [3, 9, 20, '#', '#', 15, 7]
    root = listCreatTree(None, llist, 0)
    # preOrderBT(root)
    print(Solution().findBottomLeftValue(root))

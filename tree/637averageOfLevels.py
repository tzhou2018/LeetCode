'''
@Time    : 2020/2/26 21:05
@FileName: 637averageOfLevels.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        curLayerNode = []
        res = []
        curLayerNode.append(root)
        while curLayerNode:
            curLayerValue = 0
            nextLayerNode = []
            sumCurLayerNode = len(curLayerNode)
            while curLayerNode:

                node = curLayerNode.pop(0)
                curLayerValue += node.val
                if node.left:
                    nextLayerNode.append(node.left)
                if node.right:
                    nextLayerNode.append(node.right)
            curLayerNode = nextLayerNode
            res.append(round(curLayerValue / sumCurLayerNode, 1))
        return res


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
    llist = [3, 9, 20, '#', '#', 15, 7]
    root = listCreatTree(None, llist, 0)
    print(Solution().averageOfLevels(root))

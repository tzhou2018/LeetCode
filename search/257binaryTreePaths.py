'''
@Time    : 2020/3/28 19:44
@FileName: 257binaryTreePaths.py
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
    # 方法1
    # 使用递归
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def constructRoot(root, path):
            if root:
                path += str(root.val)
                # 如果当前节点是叶子节点，把路径加入到答案中
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    constructRoot(root.left, path)
                    constructRoot(root.right, path)

        paths = []
        constructRoot(root, '')
        return paths

    # 方法2
    # 通过迭代，深度优先遍历
    """
    我们维护一个队列，存储节点以及根到该节点的路径。一开始这个队列里只有根节点。
    在每一步迭代中，我们取出队列中的首节点，如果它是一个叶子节点，则将它对应的
    路径加入到答案中。如果它不是一个叶子节点，则将它的所有孩子节点加入到队列的末尾。
    当队列为空时，迭代结束。
    """
    def binaryTreePaths1(self, root):
        if not root:
            return None
        paths = []
        stack = []
        stack.append((root, str(root.val)))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return paths

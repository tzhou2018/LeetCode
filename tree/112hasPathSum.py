'''
@Time    : 2020/2/21 21:50
@FileName: 112hasPathSum.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def hasPathSum(self, root, sume):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        stack = []
        stack.append((root, [root.val]))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and sum(path) == sume:
                return True
            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if node.left:
                stack.append((node.left, path + [node.left.val]))
        return False
    # 另一种更简洁的代码
    # 对所求的路径没有要求，只要找到就返回True
    def hasPathSumII(self, root, sume):
        if not root:
            return 0
        if not root.left and not root.right and root.val == sume:
            return True
        return self.hasPathSumII(root.right, sume - root.val) or \
               self.hasPathSumII(root.left, sume - root.val)


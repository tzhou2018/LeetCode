'''
@Time    : 2020/3/17 19:09
@FileName: 95generateTrees.py
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
    # def __init__(self):


    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        return self.generate_trees(1, n)

    def generate_trees(self, start, end):
        all_trees = []
        if start > end:
            all_trees.append(None)
            return all_trees
        for i in range(start, end + 1):
            left_trees = self.generate_trees(start, i - 1)
            right_trees = self.generate_trees(i + 1, end)
            for l in left_trees:
                for r in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r
                    all_trees.append(current_tree)
        return all_trees

# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/6/2 21:12
desc:
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def nodeNum(head):
    if not head:
        return 1


def bs(node, level, high):
    # recursion terminator
    if level == high:
        return 1
    # process logic in current level
    # drill down
    """
     // 左子树为满二叉树，结果为 2 ** (h -l) -1 + 1(加上当前节点)， 递归求右子树节点
		// 右子树为满二叉树，结果为 2 ** (h -l - 1) -1 + 1(加上当前节点)， 递归求左子树
    """
    if (mostLeftLevel(node.right, level + 1) == high):
        return 1 << (high - level) + bs(node.right, level + 1, high)
    else:
        return 1 << (high - level - 1) + bs(node.left, level + 1, high)
    # reverse the current level status if needed


# node 结点所在层，树的高度
def mostLeftLevel(node, level):
    while node:
        level += 1
        node = node.left
    return level - 1

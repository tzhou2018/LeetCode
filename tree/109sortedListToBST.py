'''
@Time    : 2020/3/1 20:33
@FileName: 109sortedListToBST.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        preMid = self.cutList(head)
        mid = preMid.next
        preMid.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

    # 将链表分隔为两段, 返回 slow 指针的前一个结点
    def cutList(self, head):
        slow = head
        fast = head.next
        pre = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        return pre

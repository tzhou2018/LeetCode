"""
@Time    : 2020/3/15 20:40
@FileName: 141hasCycle.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 思路：
    # 使用双指针，快的一次走两个，慢的一次走一次，若快指针能够赶上慢指针，则存在环
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        p = head
        q = head.next
        while p and q and q.next:
            if p == q:
                return True
            else:
                p = p.next
                q = q.next.next
        return False
    # 遍历链表，同时将所遍历的结点保存到列表中，然后判断列表中有没有该元素

    def hasCycle2(self, head):
        if not head:
            return False
        nodeList = []
        p = head
        while p:
            if p not in nodeList:
                nodeList.append(p)
                p = p.next
            else:
                return True
        return False

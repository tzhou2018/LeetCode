'''
@Time    : 2020/2/18 13:18
@FileName: 160getIntersectionNode.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        cur1, cur2 = headA, headB
        while cur2 != cur1:
            print(cur1, cur2)
            cur1 = cur1.next if cur1 is not None else headB
            cur2 = cur2.next if cur2 is not None else headA
        if cur2 == cur1:
            # print(cur2.val, cur1.val)
            return cur2
        else:
            return None



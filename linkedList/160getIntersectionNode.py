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


# 方法2
# 假设链表1 有n个结点，链表2有m个结点
# 先让长的走 |n-m| 步，之后同步走，遇到相同的结点即为相交结点
class Solution2:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        count = 0
        p1 = headA
        while p1:
            count += 1
            p1 = p1.next
        p2 = headB
        while p2:
            count -= 1
            p2 = p2.next
        p1 = headA if count > 0 else headB
        p2 = headB if p1 == headA else headA
        while abs(count) > 0:
            p1 = p1.next
            count -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

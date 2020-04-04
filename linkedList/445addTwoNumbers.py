'''
@Time    : 2020/2/18 19:08
@FileName: 445addTwoNumbers.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 思路
# 先反转所给列表，在逆序相加，之后继续反转
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        l1 = self.reverseLinked(l1)
        l2 = self.reverseLinked(l2)
        head = self.reverseOrderAdd(l1, l2)
        head = self.reverseLinked(head)
        return head

    # 逆序相加（从左往右相加）
    def reverseOrderAdd(self, l1, l2):
        head = move = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            move.next = ListNode(carry % 10)
            carry = carry // 10
            move = move.next
        return head.next

    # 反转列表
    def reverseLinked(self, head):
        if not head and not head.next:
            return head
        node = ListNode(-1)
        # node.next = None
        while head:
            q = head.next
            head.next = node.next
            node.next = head
            head = q
        return node.next


if __name__ == '__main__':
    pHead1 = ListNode(0)
    p = pHead1
    for i in range(3):
        node = ListNode(i + 5)
        p.next = node
        p = node
    p = pHead2 = ListNode(0)
    for i in range(4):
        node = ListNode(i + 6)
        p.next = node
        p = node
    head = Solution().addTwoNumbers(pHead1.next, pHead2.next)
    while head:
        print(head.val, end='\t')
        head = head.next

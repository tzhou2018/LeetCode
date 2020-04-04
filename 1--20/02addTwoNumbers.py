'''
@Time    : 2020/2/6 22:08
@FileName: 02addTwoNumbers.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = move = ListNode(0)
        # 表示进位
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
        print(head.val)
        head = head.next

"""
@Time    : 2020/7/28 21:19
@FileName: 86partition.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
将列表分为两个链表，小于x为一个，大于等于为一个；
之后将两列表进行拼接
"""
class Solution:
    def partition(self, head: ListNode, x: int):
        if not head:
            return None
        sH = None
        sT = None
        equalAndBigH = None
        equalAndBigT = None
        while head:
            next = head.next
            if head.val < x:
                head.next = None
                if not sH:
                    sH = head
                else:
                    sT.next = head
                sT = head
            else:
                head.next = None
                if not equalAndBigH:
                    equalAndBigH = head
                else:
                    equalAndBigT.next = head
                equalAndBigT = head
            head = next

        if sT:
            sT.next = equalAndBigH
            return sH

        else:
            return equalAndBigH


if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(2)
    head1.next.next.next.next = ListNode(5)
    head1.next.next.next.next.next = ListNode(2)
    head2 = head1
    head = Solution().partition(head1,3)
    print(head)
    # print(head.val)
    while head:
        print(head.val, end="\t")
        head = head.next



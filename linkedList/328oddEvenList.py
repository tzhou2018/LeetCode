'''
@Time    : 2020/2/19 10:38
@FileName: 328oddEvenList.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 将所有的奇数结点，偶数节点分别串联起来组成各自的链表
# 连接奇数结点链表和偶数结点链表；
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        moveOven = even
        while moveOven and moveOven.next:
            odd.next = moveOven.next
            odd = moveOven.next
            moveOven.next = odd.next
            moveOven = odd.next
        odd.next = even
        return head


if __name__ == '__main__':
    pHead1 = ListNode(0)
    p = pHead1
    for i in range(1, 5):
        node = ListNode(i)
        p.next = node
        p = node
    head = Solution().oddEvenList(pHead1)
    while head:
        print(head.val, end='\t')
        head = head.next

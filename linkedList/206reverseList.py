'''
@Time    : 2020/2/18 14:20
@FileName: 170reverseList.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 头插法
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pHead = ListNode(0)
        pHead.next = None
        while head:
            p = head.next
            head.next = pHead.next
            pHead.next = head
            head = p
        return pHead.next

    # 使用递归
    def reversedList_recursive(self, head):
        if not head or not head.next:
            return head
        next = head.next
        newHead = self.reversedList_recursive(head.next)
        next.next = head
        head.next = None
        return newHead


if __name__ == '__main__':
    pHead = ListNode(1)
    p = pHead
    for i in range(2, 11):
        node = ListNode(i)
        p.next = node
        p = node
    p = pHead
    while p is not None:
        print(p.val, end='\t')
        p = p.next
    print('\n')
    p = Solution().reverseList(pHead)
    while p is not None:
        print(p.val, end='\t')
        p = p.next

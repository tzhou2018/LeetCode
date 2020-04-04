'''
@Time    : 2020/2/13 21:31
@FileName: 19removeNthFromEnd.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 为了操作方便，我们引入头结点。
# 首先 p 指针移动 n 个节点，之后 p, q 指针同时移动，
# 若 p.next 为空，满足条件，删除倒数第 n 个节点，返回head.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pHead = ListNode(-1)
        pHead.next = head
        p = pHead
        q = pHead
        print("p->next->next:", p.next.val)
        # p.next = head
        for i in range(n):
            if p.next:
                p = p.next
            else:
                return None
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return pHead.next


if __name__ == '__main__':
    pHead = ListNode(-1)
    p = pHead
    for i in range(10):
        node = ListNode(i)
        p.next = node
        p = node
    head = Solution().removeNthFromEnd(ListNode(1), 1)
    while head:
        print(head.val)
        head = head.next

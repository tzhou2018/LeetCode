'''
@Time    : 2020/2/18 18:41
@FileName: 24swapPairs.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        node = ListNode(-1)
        node.next = head
        pre = node
        while pre.next and pre.next.next:
            l1 = pre.next
            l2 = pre.next.next
            next = l2.next
            l1.next = next
            l2.next = l1
            pre.next = l2
            pre = l1
        return node.next

def create_linked_list(arr=None):
    """
    根据输入的数组建立一个链表
    :param arr: 输入的数组
    :return: 链表的头指针
    """
    pHead = ListNode(arr[0])
    p = pHead
    for i in arr[1:]:
        node = ListNode(i)
        p.next = node
        p = node
    return pHead


def print_linked_list(pHead):
    """
    打印链表
    :param pHead: 链表的头结点
    :return: None
    """
    p = pHead
    while p:
        print(p.val, end='\t')
        p = p.next
    print()


if __name__ == '__main__':
    pHead = create_linked_list(arr=[1, 2, 3, 4])
    print_linked_list(pHead)
    head = Solution().swapPairs(pHead)
    print_linked_list(head)

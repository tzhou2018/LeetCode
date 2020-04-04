'''
@Time    : 2020/2/18 15:09
@FileName: 83deleteDuplicates.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 递归方法
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head

    # 非递归
    def deleteDuplication(self, pHead):
        # write code here
        first = ListNode(-1)
        first.next = pHead
        cur = pHead
        while cur and cur.next:
            if cur.val == cur.next.val:
                last = cur
                val = cur.val
                while cur and val == cur.val:
                    cur = cur.next
                last.next = cur
            else:
                cur = cur.next
        return first.next


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
    new_pHead = Solution().deleteDuplication(pHead)
    print_linked_list(new_pHead)

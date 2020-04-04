'''
@Time    : 2020/2/18 19:58
@FileName: 234isPalindrome.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 1) 将链表切分为两段
# 2）后一段反转
# 3) 判断

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 如果是偶数节点，slow 移动一个位置
        if fast:
            slow = slow.next
        self.cutList(head, slow)
        head2 = self.reverseList(slow)
        return self.isEquel(head, head2)

    def cutList(self, head, cutNode):
        while head.next != cutNode:
            head = head.next
        head.next = None

    def reverseList(self, head):
        node = None
        while head:
            p = head.next
            head.next = node
            node = head
            head = p
        return node

    def isEquel(self, head1, head2):
        while head1 and head2:
            if head1.val != head2.val:
                return False
            else:
                head1 = head1.next
                head2 = head2.next
        return True


if __name__ == '__main__':

    pHead = ListNode(1)
    p = pHead
    for i in [0, 0]:
        node = ListNode(i)
        p.next = node
        p = node
    print(Solution().isPalindrome(pHead))

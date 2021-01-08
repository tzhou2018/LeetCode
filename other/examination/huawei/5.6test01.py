'''
@Time    : 2020/5/6 20:03
@FileName: 5.6test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
给定一个排序链表，针对每个元素，增加节点或者删除节点，使得每个元素出现3次

注意：此类题不一定需要用链表结构实现，如果数组结构好做的好，可以直接写，
也是可以通过的。
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def fun1(self):
        arr = list(map(int, input().strip().split()))
        head = Node(-1)
        # head.next = None
        p = head
        for i in range(len(arr)):
            node = Node(arr[i])
            p.next = node
            p = node
        # 删除重复节点
        head = self.deleteDuplication(head.next)
        p = head
        while p:
            count = 1
            val = p.val
            q = p.next
            while count < 3:
                node = Node(val)
                p.next = node
                p = node
                count += 1
            p.next = q
            p = q
        return head

    # 删除重复的节点
    # 如：
    # 输入: 1->1->2
    # 输出: 1->2
    def deleteDuplication(self, pHead):
        # write code here
        first = Node(-1)
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


class Solution2:
    def fun2(self):
        arr = [1, 2, 3]
        head = Node(-1)
        # head.next = None
        p = head
        for i in range(len(arr)):
            node = Node(arr[i])
            p.next = node
            p = node
        head = head.next
        cur = head
        # while cur:
        #     print(cur.val, end=' ')
        #     cur = cur.next
        count = 0

        while cur:
            count = 1
            val = cur.val
            while count < 3 and cur.next:
                if val == cur.next.val:
                    cur = cur.next
                    count += 1
                else:
                    node = Node(val)
                    q = cur.next
                    cur.next = node
                    node.next = q
                    cur = node
                    count += 1
            if cur.next and cur.val == cur.next.val:
                last = cur
                val = cur.val
                while cur and val == cur.val:
                    cur = cur.next
                last.next = cur
            else:
                cur = cur.next
        # if cur
        return head


if __name__ == '__main__':
    head = Solution2().fun2()
    while head:
        print(head.val, end=' ')
        head = head.next

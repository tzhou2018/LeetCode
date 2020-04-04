'''
@Time    : 2020/2/18 21:29
@FileName: 725splitListToParts.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
按照题意，首先求出链表中节点个数count：

如果count <= k，表示每个子节点存在于结果数组中；

如果k > count，把链表分为k份，每份至少有count/k个元素，未分配元素为count%k，
因为未分配元素在范围为[0,k)，所以给每份元素数从前到后+1，以满足题目条件

如果8个元素分成3分，每份至少有8/3=2个元素，即[2,2,2]，剩余8%3=2个元素，分给第一份和第二份，为[3,3,2]
"""
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        count = 0
        cur = root
        while cur:
            count += 1
            cur = cur.next
        mod = count % k
        size = count // k
        ret = [None] * k
        cur, index = root, 0
        while cur:
            ret[index] = cur
            if mod > 0:
                curSize = size + 1
                mod -= 1
            else:
                curSize = size
            for i in range(curSize - 1):
                cur = cur.next
            nextNode = cur.next
            cur.next = None
            cur = nextNode
            index += 1
        return ret

'''
@Time    : 2020/3/16 21:36
@FileName: 605canPlaceFlowers.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
我们从左到右扫描数组 flowerbed，如果数组中有一个 0，并且这个 0 的左右两侧都是 0，
那么我们就可以在这个位置种花，即将这个位置的 0 修改成 1，并将计数器 count 增加 1。
对于数组的第一个和最后一个位置，我们只需要考虑一侧是否为 0。

在扫描结束之后，我们将 count 与 n 进行比较。如果 count >= n，那么返回 True，否则返回 False。
参考链接：https://leetcode-cn.com/problems/can-place-flowers/solution/chong-hua-wen-ti-by-leetcode/
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt = 0
        lenFlo = len(flowerbed)
        for i in range(lenFlo):
            if flowerbed[i] == 1:
                continue
            if cnt < n:
                pre = 0 if i == 0 else flowerbed[i - 1]
                next = 0 if i == lenFlo -1 else flowerbed[i + 1]
                if pre == 0 and next == 0:
                    cnt += 1
                    flowerbed[i] = 1
            else:
                return True
        return cnt >= n

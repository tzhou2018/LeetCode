'''
@Time    : 2020/3/15 16:19
@FileName: 345reverseVowels.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
使用双指针，一个指针从头向尾遍历，一个指针从尾到头遍历，当两个指针都遍历到元音字符时，交换这两个元音字符。

为了快速判断一个字符是不是元音字符，我们将全部元音字符添加到集合 HashSet 中，从而以 O(1) 的时间复杂度进行该操作。

时间复杂度为 O(N)：只需要遍历所有元素一次
空间复杂度 O(1)：只需要使用两个额外变量
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowerls = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        s = list(s)
        right = len(s) - 1
        while left < right:
            if s[left] in vowerls:
                if s[right] in vowerls:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return ''.join(s)

    # 思路同上述方法
    def reverseVowels1(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowerls = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        s = list(s)
        right = len(s) - 1
        while left < right:
            while left < right and s[left] not in vowerls:
                left += 1
            while left < right and s[right] not in vowerls:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)


if __name__ == '__main__':
    print(Solution().reverseVowels("hello"))

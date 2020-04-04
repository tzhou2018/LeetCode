'''
@Time    : 2020/3/15 19:27
@FileName: 680validPalindrome.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
使用双指针可以很容易判断一个字符串是否是回文字符串：
令一个指针从左到右遍历，一个指针从右到左遍历，这两个指针同时移动一个位置，
每次都判断两个指针指向的字符是否相同，如果都相同，字符串才是具有左右对称性质的回文字符串。

本题的关键是处理删除一个字符。在使用双指针遍历字符串时，如果出现两个指针指向的字符不相等的情况，
我们就试着删除一个字符，再判断删除完之后的字符串是否是回文字符串。
在判断是否为回文字符串时，我们不需要判断整个字符串，因为左指针左边
和右指针右边的字符之前已经判断过具有对称性质，所以只需要判断中间的子字符串即可。
在试着删除字符时，我们既可以删除左指针指向的字符，也可以删除右指针指向的字符。
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) \
                       or self.isPalindrome(s, left, right - 1)
            else:
                left += 1
                right -= 1
        return True

    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    print(Solution().validPalindrome("aba"))

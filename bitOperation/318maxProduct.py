'''
@Time    : 2020/3/14 15:40
@FileName: 318maxProduct.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 思路：
# 本题主要是判断两个字符串中是否有相同的字符。
# 通过异或 或运算将字母是否出现，表示出来；通过与运算来判断两个单词是否含有相同字符；
# 由于是不含大写的26个小写字母，于是我们可以用26位二进制来表示该单词中含有哪些字母，
# 例如 "abdf"对应的二进制位 101011
#
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bitMap = [0] * len(words)
        wordsLen = len(words)
        ret = 0
        for i in range(wordsLen):
            for word in words[i]:
                bitMap[i] |= 1 << (ord(word) - ord('a'))
        for i in range(wordsLen):
            for j in range(i):
                if bitMap[j] & bitMap[i] == 0:
                    ret = max(ret, len(words[i]) * len(words[j]))
        return ret

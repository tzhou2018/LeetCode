'''
@Time    : 2020/2/10 20:26
@FileName: isMatch.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

# 思路：
# 当模式中的第二个字符是“*”时：
# 如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，继续匹配。
# 如果字符串第一个字符跟模式第一个字符匹配，可以有3种匹配方式：
# 1、模式后移2字符，相当于x*被忽略；
# 2、字符串后移1字符，模式后移2字符；
# 3、字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位；

# 当模式中的第二个字符不是“*”时：
# 1、如果字符串第一个字符和模式中的第一个字符相匹配，
# 那么字符串和模式都后移一个字符，然后匹配剩余的。
# 2、 如果 字符串第一个字符和模式中的第一个字符相不匹配，直接返回false。
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if len(s) > 0 and not p:
            return False
        if len(p) > 1 and p[1] == '*':
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[2:]) \
                       or self.isMatch(s[1:], p[:]) \
                       or self.isMatch(s[:], p[2:])
            else:
                return self.isMatch(s, p[2:])
        if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        return False


if __name__ == '__main__':
    print(Solution().isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c'))

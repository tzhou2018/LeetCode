'''
@Time    : 2020/2/10 20:26
@FileName: isMatch.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


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

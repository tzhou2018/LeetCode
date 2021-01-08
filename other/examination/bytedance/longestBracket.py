'''
@Time    : 2020/3/31 22:47
@FileName: longestBracket.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 最长有效括号
# 暴力法，同上一道题，就是最开始把第一个字符当做
# 最长有效括号的首字符来遍历字符串，接着把第二个
# 字符当做最长有效括号的首字符来遍历字符串，接着把第三个字符......
class Solution:

    def longestValidParentheses(self, s):
        if not s:
            return 0
        sLen = len(s)
        Max = 0
        for i in range(sLen):
            for j in range(i + 2, sLen + 1, 2):
                if self.isValid(s[i:j]):
                    Max = max(Max, j - i)
        return Max

    def isValid(self, s):
        if not s:
            return 0
        sLen = len(s)
        count = 0
        for i in range(sLen):
            c = s[i]
            if c == '(':
                count += 1
            elif count == 0:
                return False
            else:
                count -= 1
        return count == 0


# 对上面的解法进行优化
# 这次我们往栈里存储元素下标
"""
1、先把 -1 放入栈内。（至于为什么？看到后面你就知道了） 
2、对于遇到的每个 '(' ，我们将它的下标放入栈中。 
3、对于遇到的每个 ‘)’ ，我们弹出栈顶的元素并将当前元素的下标与弹出元素下标作差，
得出当前有效括号字符串的长度。
"""


class Solution1:

    def longestValidParentheses(self, s):
        if not s:
            return
        sLen = len(s)
        stack = [-1]
        Max = 0
        for i in range(sLen):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    Max = max(Max, i - stack[-1])
        return Max

    # 对上述解法在进行空间优化
    """
    从左到右遍历字符串的过程中，用 left 记录 '(' 的数量，用 right 记录 ')' 的数量。并且在遍历的过程中：
    1、如果 left == right，显然这个时候 right 个 ')' 都将一定能够得到匹配。所以当前的有效括号长度为 2 * left。然后更新 max。
    2、如果 left < right，显然这个时候部分 ')' 一定得不到匹配，此时我们把 left 和 right 都置为 0。
    由于'(' ')' 是等价的，还需要从右进行遍历，更新max
    """

    def longestValidParentheses1(self, s):
        if not s:
            return 0
        left, right = 0, 0
        Max = 0
        sLen = len(s)
        # 从左边遍历
        for i in range(sLen):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                Max = max(Max, 2 * left)
            elif right > left:
                left, right = 0, 0
        # 从右边遍历
        left, right = 0, 0
        for i in range(sLen - 1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            if right == left:
                Max = max(Max, 2 * right)
            elif left > right:
                left, right = 0, 0
        return Max

# 动态规划
class Solution3:
    def maxLength(self, str):
        if not str:
            return 0
        strLen = len(str)
        dp = [0] * strLen
        pre = 0
        res = 0

        for i in range(1, strLen):
            if str[i] == ')':
                pre = i - dp[i - 1] - 1
                if pre >= 0 and str[pre] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[pre - 1] if pre > 0 else 0)
            res = max(res, dp[i])
        return res


if __name__ == '__main__':
    print(Solution1().longestValidParentheses1("(()"))
    print(Solution3().maxLength("(()"))

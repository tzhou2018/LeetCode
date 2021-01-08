'''
@Time    : 2020/5/7 19:54
@FileName: longestPalindrome.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
"""
    事实上，只需使用恒定的空间，我们就可以在 O(n2) 的时间内解决这个问题。
    我们观察到回文中心的两侧互为镜像。因此，回文可以从它的中心展开，
    并且只有 2n -1 个这样的中心。    
    你可能会问，为什么会是 2n -1 个，而不是 n 个中心？
    原因在于所含字母数为偶数的回文的中心可以处于两字母之间（例如 "abba" 的中心在两个 "b" 之间）。
    """


# 123432156787652222
def fun1():
    s = input().strip()
    start, end = 0, 0
    res = []
    Max = 0
    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        lenSubstring = max(len1, len2)
        # if lenSubstring == Max:
        #     res.append(s[start:end + 1])
        if lenSubstring > (end - start):
            Max = max(Max, lenSubstring)
            start = i - (lenSubstring - 1) // 2
            end = i + lenSubstring // 2
            # res.clear()
        if lenSubstring >= Max:
            res.append(s[start:end + 1])
        # if lenSubstring == Max:
        #     res.append(s[start:end + 1])
    if Max == 1:
        print("null")
        # return None
    else:
        for e in res:
            if len(e) >= Max:
                print(e)


def expandAroundCenter(s, left, right):
    L, R = left, right
    while (L >= 0 and R < len(s) and s[L] == s[R]):
        L -= 1
        R += 1
    return R - L - 1


if __name__ == '__main__':
    # print(fun1())
    fun1()

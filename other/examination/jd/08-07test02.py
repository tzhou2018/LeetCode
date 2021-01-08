"""
@Time    : 2020/8/6 20:40
@FileName: 08-07test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""
"""
现有一个正整数，希望去掉这个数中某一个数字之后可以得到一个回文素数。

回文素数是指一个素数同时还是一个回文数（回文数即从左到右和从右到左均一样的数，例如12321）。【注意：一位数也被认为是回文数】

输入两个正整数N和M，满足N<M，请编写一个程序统计N和M之间存在多少个满足上述要求的数？


"""

def test():
    n, m = list(map(int, input().strip().split(" ")))
    count = 0
    for i in range(n, m + 1):
        strN = getNumList(i)
        if valid(strN):
            count += 1
    return count


def valid(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return isPalindrom(s, left + 1, right) or isPalindrom(s, left, right - 1)
        else:
            left += 1
            right -= 1
    return True


def isPalindrom(s, left, right):
    if s[0] == "0":
        s = s[1:]
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def getNumList(n):
    res = ""
    while n > 0:
        res += str(n % 10)
        n = n // 10
    # print(res)
    res = res[::-1]
    if res[0] == "0":
        return res[1:]
    return res


if __name__ == '__main__':
    print(test())

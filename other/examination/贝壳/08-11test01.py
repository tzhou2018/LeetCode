"""
@Time    : 2020/8/11 19:04
@FileName: 08-11test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""

# 最多可以改变几个字符使原字符变为回文
def test01():
    n = int(input())
    arr = list(input().strip())
    count = 0
    start = 0
    end = n - 1
    while start < end:
        if arr[start] != arr[end]:
            count += 1
        start += 1
        end -= 1
    return count


if __name__ == '__main__':
    res = test01()
    print(res)

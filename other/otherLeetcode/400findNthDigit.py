"""
@Time       : 2020/9/10 14:28
@FileName   : 400findNthDigit.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


def findNthDigit(n):
    """
    digits 表示这个数字对应的几位数
    target 表示这个数字对应的数值，最后确定返回值是target中的哪个数字；
    :param n:
    :return:
    """

    base = 9
    digits = 1
    while n - base * digits > 0:
        n -= base * digits
        base *= 10
        digits += 1
    index = n % digits
    if index == 0:
        index = digits
    number = 1
    for i in range(1, digits):
        number *= 10
    number += n // digits
    if index == digits:
        number -= 1
    for i in range(index, digits):
        number //= 10
    return number % 10


# 法2
# 思路同上述代码，只是做个简化
def findNthDigit2(n):
    n -= 1
    for i in range(1, 11):
        first_num = pow(10, i - 1)
        if n < 9 * first_num * i:
            return int(str(first_num + n // i)[n % i])
        n -= 9 * first_num * i


if __name__ == '__main__':
    res = findNthDigit(365)
    print(res)
    # sol = Solution()
    # res = sol.findNthDigit(3)
    # print(res)
    print(findNthDigit2(365))

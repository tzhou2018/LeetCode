'''
@Time    : 2020/4/23 14:28
@FileName: yuanjing.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
牛牛相对一个数做若干次变换，直到这个数只剩下以为数字。
变换的规则是：将这个数变成所有位数上的数字的乘积。比如285经过一次变换后转换成2*8*5 = 80
问题是，要做多少次这样的变化，使得这个数变成个位数。
"""
def fun1():
    n = int(input().strip())
    count = 0
    # muti = float('inf')
    while n // 10 > 0 :
        temp = n
        muti = 1
        while temp > 0:
            res = temp % 10
            muti *= res
            temp = temp // 10
        count += 1
        n = muti
    print(count)


if __name__ == '__main__':
    fun1()

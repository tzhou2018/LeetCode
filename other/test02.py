'''
@Time    : 2020/4/29 11:13
@FileName: 08-08test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
import sys


def foo(*args, **kwargs):
    print('args=', args, "len:", len(args))
    print('kwargs=', kwargs, "len:", len(kwargs))
    print('**********************')


if __name__ == '__main__':
    foo(1, 2, 3)
    foo(a=1, b=2, c=3)
    foo(1, 2, 3, a=1, b=2, c=3)
    foo(1, 'b', 'c', a=1, b='b', c='c')

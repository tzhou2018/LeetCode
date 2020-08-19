'''
@Time    : 2020/3/27 20:54
@FileName: swopString.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
首先判断字符串S能否转换为T，即判断S和T中字符出现的次数是都完全一致
接下来寻找S中不需要移动的字符数，即寻找T的最长的一个首部，
满足：S中可以找到一个子序列，包含此首部中出现的所有字符，
并且这些字符出现的顺序相同。不需要移动的字符数即为此首部的长度。

如上例中T满足要求的最长首部为cd，对应S中的子序列为ckd。

输出需要操作的次数，即为T的长度减去不需要移动的字符数
"""
import sys
def func(S, T):
    hashmap = {}
    # 首先统计每个字符串出现的次数是否相等
    for e in S:
        hashmap[e] = hashmap.get(e, 0) + 1
    for e in T:
        if e in hashmap:
            hashmap[e] -= 1
        else:
            return -1
    for k, v in hashmap.items():
        if v != 0:
            return -1
    # 然后寻找不需要移动的字符串
    i, j = 0, 0
    while i < len(S) and j < len(T):
        while i < len(S) and S[i] != T[j]:
            i += 1
        i += 1
        j += 1
    return len(T) - j


if __name__ == '__main__':
    S = sys.stdin.readline().strip()
    T = sys.stdin.readline().strip()
    print(func(S, T))

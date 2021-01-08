# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/8/28 21:17
desc:
'''
if __name__ == '__main__':
    # print(1 + " " + 1)
    nums = int(input().strip())
    for i in range(nums):
        color = list(input().strip())
        from collections import OrderedDict

        d = OrderedDict()
        later = color[0]
        i = 1
        cnt = 0
        maxlen = 0
        for item in color:
            if item == later:
                cnt += 1
            else:
                d[i] = [later, cnt]
                maxlen = max(cnt, maxlen)
                later = item
                cnt = 1
                i += 1
        d[i] = [later, cnt]
        maxlen = max(cnt, maxlen)
        # print(d)
        length = 0
        for i in range(1, len(d.values()) - 1):
            if d[i][0] == d[i + 2][0] and d[i + 1][1] == 1:
                now = d[i][1] + 1 + d[i + 2][1]
                length = max(now, length)
        # print(length)
        new = 0
        if len(d.values()) > 1:
            for item in d.values():
                new = max(new, item[1] + 1)
        print(max(maxlen, length, new))

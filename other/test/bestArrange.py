# coding=utf-8
# -*- coding:utf-8 -*-
'''
Author: Solarzhou
Email: t-zhou@foxmail.com

date: 2020/6/6 15:13
desc:
'''
import functools


class Program:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    # 定义一个比较器
    def compare(self, o1, o2):
        return o1.end - o2.end

    def bestArrange(self, startM, endM, start):
        programs = []
        for i in range(len(endM)):
            programs.append(Program(startM[i], endM[i]))
        programs = sorted(programs, key=functools.cmp_to_key(self.compare))
        res = 0
        for pro in programs:
            if pro.start >= start:
                res += 1
                start = pro.end
        return res


if __name__ == '__main__':
    starts = [3, 3, 3, 5, 7]
    ends = [4, 5, 4, 6, 8]
    print(Program(0, 0).bestArrange(starts, ends, 1))

"""
@Time    : 2020/8/20 20:48
@FileName: 08-20test02.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""

"""
赏金猎人
时间限制： 3000MS
内存限制： 786432KB
题目描述：
克里森是一名赏金猎人，他平时需要完成一些任务赚钱。最近他收到了一批任务，
但是受到时间的限制，他只能完成其中一部分。具体来说就是有n个任务，
每个任务用l, r, w来表示任务开始的时间l，结束的时间r和完成任务获得的金钱。

克里森是个贪心的人，他想知道自己在任务不冲突的情况下最多获得多少金钱。

输入描述
第一行一个数n表示任务的个数。(1≤n≤1e3)

接下来n行每行三个整数l, r, w表示第i个任务的开始时间，结束时间，以及收益。(1≤l≤r≤1e6,1≤w≤1e9)
"""


def test02():
    n = int(input().strip())
    jobs = []
    for i in range(n):
        jobs.append(list(map(int, input().strip().split(" "))))
    jobs.sort(key=lambda x: (x[1], -x[2]))
    dp = [0] * n
    dp[0] = jobs[0][2]
    for i in range(1, n):
        begin = 0
        while jobs[begin][1] < jobs[i][0]:
            begin += 1
        if begin >= 1:
            dp[i] = dp[i - 1] + jobs[i][2]
        else:
            dp[i] = max(dp[i - 1], jobs[i][2])
    print(dp)
    print(dp[-1])


if __name__ == '__main__':
    test02()

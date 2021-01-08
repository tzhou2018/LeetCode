"""
@Time    : 2020/8/20 20:27
@FileName: 08-20test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
"""

"""
服务器管理
时间限制： 3000MS
内存限制： 786432KB
题目描述：
小A的购买了一批服务器，他准备将这些服务器租用出去。每一个服务器有一个固定的带宽，
人们根据自己需要的带宽来租用这些服务器。一台服务器只能租给一个人。

小A现在有n个空闲的服务器，第 i 个服务器拥有ai的带宽。有m个客户来租服务器，
第 i 位客户需要带宽至少为bi的服务器，并且愿意花ci元作为预算。
（服务器带宽独立不可叠加，若不能成功租出则输出0） 小A可以选择拒绝一些人，
现在，小A想知道自己的服务器最多能租多少钱？
"""


def test01():
    n, m = list(map(int, input().strip().split(" ")))
    server = list(map(int, input().strip().split(" ")[:n]))
    clients = []
    for i in range(m):
        clients.append(list(map(int, input().strip().split(" "))))
    server.sort()
    clients.sort(key=lambda x: (x[0], -x[1]))
    res = 0
    flag = [False] * len(clients)
    for i in range(n):
        temp = 0
        b = -1
        for j in range(m):
            if not flag[j] and server[i] >= clients[j][0]:
                if clients[j][1] > temp:
                    temp = clients[j][1]
                    b = j
        if b > -1:
            res += temp
            flag[b] = True
    print(res)
    return res


if __name__ == '__main__':
    test01()

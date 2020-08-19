'''
@Time    : 2020/4/25 16:00
@FileName: dijkstra.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
最短路径
迪杰斯特拉算法
参考文章：知乎专栏 https://zhuanlan.zhihu.com/p/63395403
"""


def startWith(start, mGraph):
    # 已经过的点
    passed = [start]
    # 未经过的点
    noPass = [i for i in range(len(mGraph)) if i != start]
    res = mGraph[start]
    while len(noPass):
        idX = noPass[0]
        for i in noPass:
            if res[i] < res[idX]:
                idX = i
        noPass.remove(idX)
        passed.append(idX)
        for i in noPass:
            if res[idX] + mGraph[idX][i] < res[i]:
                res[i] = res[idX] + mGraph[idX][i]
    return res


if __name__ == '__main__':
    inf = 10086
    mgraph = [[0, 1, 12, inf, inf, inf],
              [inf, 0, 9, 3, inf, inf],
              [inf, inf, 0, inf, 5, inf],
              [inf, inf, 4, 0, 13, 15],
              [inf, inf, inf, inf, 0, 4],
              [inf, inf, inf, inf, inf, 0]]

    dis = startWith(0, mgraph)
    print(dis)

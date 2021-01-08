"""
@Time       : 2020/9/5 15:49
@FileName   : 09_05test02.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


# import functools
#
#
# class Product:
#     def __init__(self, name, cost, rate):
#         self.name = name
#         self.cost = cost
#         self.rate = rate
#
#
# def maxRateComparator(o1, o2):
#     return o2.rate - o1.rate
#
#
# def test02():
#     temp = input().strip().split(",")
#     total = int(temp[1])
#     nodes = []
#     while True:
#         temp = input().strip().split(",")
#         if temp[0] == "null":
#             break
#         nodes.append(Product(temp[0], int(temp[1]), float(temp[2])))
#
#     nodes1 = sorted(nodes, key=functools.cmp_to_key(maxRateComparator))
#     while total > 0:
#         pass


# ------------------
def test02_02():
    temp = input().strip().split(",")
    total = int(temp[1])
    names = []
    vals = []
    wts = []
    counts = []
    while True:
        temp = input().strip()
        if temp == "null":
            break
        else:
            temp = temp.split(",")
            names.append(temp[0])
            vals.append(float(temp[2][:-1]))
            wts.append(int(temp[1]))
    print(names)
    print(wts)
    print(vals)
    counts = [0] * len(names)
    dp = [[0] * (total + 1) for _ in range(len(names) + 1)]
    for i in range(1, len(names) + 1):
        for j in range(1, total + 1):
            if j < wts[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                if dp[i - 1][j - wts[i - 1]] + vals[i - 1] > dp[i - 1][j]:

                    dp[i][j] = dp[i - 1][j - wts[i - 1]] + vals[i - 1]
                    counts[i - 1] += wts[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
                # dp[i][j] = max(dp[i-1][j],dp[i-1][j-wts[i-1]] + vals[i-1])
    print("最大值：%f" % dp[-1][-1])
    for i in range(len(names)):
        if counts[i] != 0:
            print(names[i] + "," + str(counts[i]))


if __name__ == '__main__':
    test02_02()
"""
total,78
新网1号,5,2.5%
新网2号,12,2.5%
新网3号,16,2.6%
新网4号,17,2.7%
null
"""

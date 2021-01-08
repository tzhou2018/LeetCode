"""
@Time       : 2020/9/5 19:25
@FileName   : 09_05test02.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回能创建的房屋数
# @param t int整型 要建的房屋面宽
# @param xa int整型一维数组 已有房屋的值，其中 x0 a0 x1 a1 x2 a2 ... xi ai 就是所有房屋的坐标和房屋面宽。 其中坐标是有序的（由小到大）
# @return int整型
#
class Solution:
    def getHouses(self, t, xa):
        # write code here
        diff = []
        count = 0
        for i in range(0, len(xa), 2):
            n1 = xa[i]
            n2 = xa[i + 1] / 2
            diff.append([n1 - n2, n1 + n2])
        start = diff[0][1]
        print(diff)
        for i in range(1, len(diff)):
            if diff[i][0] - start > t:
                count += 2
            elif diff[i][0] - start == t:
                count += 1
                # start = diff[i][1]
            start = diff[i][1]

        return count + 2


if __name__ == '__main__':
    temp = input().strip()
    n = int(temp[0])
    # print(temp[1:][2:-1])
    arr = temp[1:][2:-1].split(",")
    # print(arr)
    arr = list(map(int, arr))
    # print(arr)
    solution = Solution()
    res = solution.getHouses(n, arr)
    print(res)

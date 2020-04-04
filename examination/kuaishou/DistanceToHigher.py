'''
@Time    : 2020/3/22 19:10
@FileName: DistanceToHigher.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


#
# 获取队中从前到后每个人与前方身高高于自己的人的最短距离
# @param height int整型一维数组 队中从前到后每个人与前方身高高于自己的人的最短距离
# @return int整型一维数组
#
class Solution:
    def DistanceToHigher(self, height):
        # write code here
        res = [0] * len(height)
        lenHeight = len(height)
        for i in range(lenHeight - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if height[j] > height[i]:
                    res[i] = i - j
                    break
        return res


if __name__ == '__main__':
    height = input()
    height = height[1:-1]
    height = list(map(int, height.split(',')))
    print(Solution().DistanceToHigher(height))

'''
@Time    : 2020/2/11 19:51
@FileName: 11maxArea.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 思路：
# 定义两个指针 left, right 分别指向所给列表的左右，
# 然后两指针向中间搜索，并更新面积res,直至 left== right
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        right = len(height) - 1
        left = 0
        res = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(area, res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

'''
@Time    : 2020/3/9 20:48
@FileName: 565arrayNesting.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxS = 0
        for i in range(len(nums)):
            cnt = 0
            j = i
            while nums[j] != -1:
                cnt += 1
                t = nums[j]
                # 标志该位置已经被访问
                nums[j] = -1
                j = t
            maxS = max(maxS, cnt)

        return maxS


if __name__ == '__main__':
    print(Solution().arrayNesting([0, 2, 1]))

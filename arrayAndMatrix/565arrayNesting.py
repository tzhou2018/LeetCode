'''
@Time    : 2020/3/9 20:48
@FileName: 565arrayNesting.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    # 依次将每个位置的元素作为 S 中第一个元素，遍历一遍后取最大的集合。
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

    # def array(self,nums ):
    #     maxS = 0
    #     for i in range(len(nums)):
    #         cnt = 0
    #         j = i
    #         while nums[j] != -1
    #     pass


if __name__ == '__main__':
    print(Solution().arrayNesting([5, 4, 0, 3, 1, 6, 2]))

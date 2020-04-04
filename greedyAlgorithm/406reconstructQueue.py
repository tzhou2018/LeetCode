'''
@Time    : 2020/3/16 19:23
@FileName: 406reconstructQueue.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
身高 h 降序、个数 k 值升序，然后将某个学生插入队列的第 k 个位置中。
个子矮的人相对于个子高的人是看不见的
参考文档：https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/gen-ju-shen-gao-zhong-jian-dui-lie-by-leetcode/
"""
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) == 0:
            return []
        people.sort(key=lambda l: (-l[0], l[1]))
        res = []
        for e in people:
            res.insert(e[1], e)
        return res


if __name__ == '__main__':
    print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

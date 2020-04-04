'''
@Time    : 2020/3/29 22:34
@FileName: 77combine.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def backTracking(first, cur):
            # terminate
            if len(cur) == k:
                output.append(cur[:])
                return
            # precess logic in current level
            # drill down
            for i in range(first, n + 1):
                cur.append(i)
                backTracking(i + 1, cur)
                # reverse the current status if needed
                cur.pop()

        output = []
        backTracking(1, [])
        return output


if __name__ == '__main__':
    print(Solution().combine(4, 2))

'''
@Time    : 2020/3/16 11:38
@FileName: 451frequencySort.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def frequencySort(self, str):
        """
        :type s: str
        :rtype: str
        """
        frequencyForNum = {}
        for s in str:
            frequencyForNum[s] = frequencyForNum.get(s, 0) + 1
        buckets = [0] * (len(str) + 1)
        for k, v in frequencyForNum.items():
            if buckets[v] == 0:
                buckets[v] = []
            buckets[v].append(k)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i] == 0:
                continue
            for e in buckets[i]:
                for j in range(i):
                    res.append(e)
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().frequencySort('tree'))

'''
@Time    : 2020/2/11 21:32
@FileName: 14longestCommonPrefix.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 取字符串数组中第一个元素，将剩下的元素依次与第一个元素进行判断；
        # 长度一次递减
        if not strs:
            return ''
        pre = strs[0]
        for s in strs:
            lenPre = len(pre)
            while s[0:lenPre] != pre:
                lenPre -= 1
                pre = pre[0:lenPre]
                if not pre:
                    return pre
        return pre


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))

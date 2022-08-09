"""
@Time       : 2020/9/5 10:26
@FileName   : 424characterReplacement.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


# 思路
# 使用长度为 26 的数组存储每个元素出现的次数。
# 使用滑动窗口，左右侧各设置left，right指针；
# 当窗口大小减去出现最多字符数据小于 k 时，右指针滑动；否则，左指针右滑并且将当前元素所在位置的个数减 1
#

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        res = 0
        maxCount = 0
        countArr = [0] * 26
        while right < len(s):
            countArr[ord(s[right]) - ord("A")] += 1
            # 当前窗口内最多字符的个数
            maxCount = max(maxCount, countArr[ord(s[right]) - ord("A")])
            # 需要替换的字符，就是当前窗口的大小减去窗口中数量最多的字符的数量
            if right - left + 1 - maxCount > k:
                # 缩小窗口
                countArr[ord(s[left]) - ord("A")] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    s = "ABAB"
    print(solution.characterReplacement(s, 2))

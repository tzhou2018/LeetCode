"""
@Time       : 2020/9/5 10:26
@FileName   : 424characterReplacement.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


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

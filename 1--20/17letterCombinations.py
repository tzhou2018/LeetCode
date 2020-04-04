'''
@Time    : 2020/2/13 19:26
@FileName: 17letterCombinations.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return ""
        numberDic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', \
                     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = [i for i in numberDic[digits[0]]]
        print(res)
        for i in digits[1:]:
            res = [m + n for m in res for n in numberDic[i]]
        return res


if __name__ == '__main__':
    print(Solution().letterCombinations('2345'))

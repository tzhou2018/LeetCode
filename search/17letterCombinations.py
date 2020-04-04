'''
@Time    : 2020/3/26 23:06
@FileName: 17letterCombinations.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

"""
方法：回溯
回溯是一种通过穷举所有可能情况来找到所有解的算法。如果一个候选解最后被发现并不是可行解，
回溯算法会舍弃它，并在前面的一些步骤做出一些修改，并重新尝试找到可行解。

给出如下回溯函数 backtrack(combination, next_digits) ，它将一个目前已经产生的组合 
combination 和接下来准备要输入的数字 next_digits 作为参数。

如果没有更多的数字需要被输入，那意味着当前的组合已经产生好了。
如果还有数字需要被输入：
遍历下一个数字所对应的所有映射的字母。
将当前的字母添加到组合最后，也就是 combination = combination + letter 。
重复这个过程，输入剩下的数字： backtrack(combination + letter, next_digits[1:]) 。

链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/dian-hua-hao-ma-de-zi-mu-zu-he-by-leetcode/

"""
class Solution:
    output = []
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # phone = {'2': ['a', 'b', 'c'],
        #          '3': ['d', 'e', 'f'],
        #          '4': ['g', 'h', 'i'],
        #          '5': ['j', 'k', 'l'],
        #          '6': ['m', 'n', 'o'],
        #          '7': ['p', 'q', 'r', 's'],
        #          '8': ['t', 'u', 'v'],
        #          '9': ['w', 'x', 'y', 'z']}
        #
        # def backtrack(combination, next_digits):
        #     # if there is no more digits to check
        #     if len(next_digits) == 0:
        #         # the combination is done
        #         output.append(combination)
        #     # if there are still digits to check
        #     else:
        #         # iterate over all letters which map
        #         # the next available digit
        #         for letter in phone[next_digits[0]]:
        #             # append the current letter to the combination
        #             # and proceed to the next digits
        #             backtrack(combination + letter, next_digits[1:])
        #
        # output = []
        if digits:
            self.backTrack("", digits)
        else:
            return []
        return self.output

    def backTrack(self, combination, next_digits):
        if len(next_digits) == 0:
            self.output.append(combination)
        else:
            for letter in self.phone[next_digits[0]]:
                self.backTrack(combination + letter, next_digits[1:])


if __name__ == '__main__':
    print(Solution().letterCombinations('2'))


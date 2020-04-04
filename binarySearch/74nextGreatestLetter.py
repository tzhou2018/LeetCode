'''
@Time    : 2020/3/17 11:46
@FileName: 74nextGreatestLetter.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if ord(letters[-1]) <= ord(target):
            return letters[0]
        high = len(letters) - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if ord(letters[mid]) > ord(target):
                high = mid - 1
            elif ord(letters[mid]) <= ord(target):
                low = mid + 1

        return letters[low]
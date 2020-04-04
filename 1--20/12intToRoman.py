'''
@Time    : 2020/2/11 20:09
@FileName: 12intToRoman.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return ''
        # 确定个十百千各自位置上的0~9对应罗马字母
        c = {
            'g': ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
            's': ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
            'b': ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
            'q': ('', 'M', 'MM', 'MMM')
        }
        roman = []
        # 用整除和取余获得个十百千对应的数字
        roman.append(c['q'][num // 1000])
        roman.append(c['b'][(num // 100) % 10])
        roman.append(c['s'][(num // 10) % 10])
        roman.append(c['g'][num % 10])

        return ''.join(roman)


if __name__ == '__main__':
    print(Solution().intToRoman(1994))

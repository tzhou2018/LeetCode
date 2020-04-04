'''
@Time    : 2020/3/13 21:06
@FileName: 260singleNumber.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''


# 思路：从位运算符中异或运算考虑：两个相同的数字异或为0，一个数与0异或依然是他本身。
# 当所给数组中只有一个数出现一次时，我们把所给数组中的所有数依次进行异或运算，
# 最后剩下的就是落单的数，因为成对的数都抵消了；

# 依照这个思路，我们来看两个数（我们假设是AB）出现一次的数组。我们首先还是先异或，剩下的数字肯定是A、B异或的结果，
# 这个结果的二进制中的1，表现的是A和B的不同的位。我们就取第一个1所在的位数，假设是第3位，接着把原数组分成两组，
# 分组标准是第3位是否为1。如此，相同的数肯定在一个组，因为相同数字所有位都相同，而不同的数，肯定不在一组。
# 然后把这两个组按照最开始的思路，依次异或，剩余的两个结果就是这两个只出现一次的数字。
# 如： 输入数组 [2,4,3,6,3,2,5,5]
# 异或计算后： 0010
# 倒数第二位是1，按这个进行分组；
# 第一组是 [2,3,6,3,2]; 第二组是 [4,5,5]
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        key = 0
        for item in nums:
            key ^= item
        num1, num2 = 0, 0
        # key 为所给数列中两个不同的树异或结果
        # 计算 key 最右边第一个不为零的位数
        key &= -key
        for num in nums:
            if num & key == 0:
                num1 ^= num
            else:
                num2 ^= num
        return num1, num2

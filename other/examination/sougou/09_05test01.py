"""
@Time       : 2020/9/5 18:41
@FileName   : 09_05test01.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回能交换奖品的最大数量
# @param a int整型
# @param b int整型
# @param c int整型
# @return int整型
#
class Solution:
    def numberofprize(self, a, b, c):
        # write code here
        mid = (a + b + c) // 3
        rightDiff = c - mid
        # c -= mid
        midDiff = b - mid
        # b -= mid
        while midDiff >= 2:
            a += 1
            midDiff -= 2
            b -= 2
        while rightDiff >= 2:
            if a <= mid and a <= b:
                a += 1
                rightDiff -= 2
                c -= 2
            elif b <= mid:
                b += 1
                rightDiff -= 2
                c -= 2
        temp = midDiff + rightDiff
        while temp == 2:
            a += 1
            temp -= 2
            if midDiff >= 1:
                b -= 1
            if rightDiff >= 1:
                c -= 1
        a, b, c = sorted([a, b, c])
        # print(a, b, c)
        if b - a >= 2 and c - a >= 2:
            a += 1
            b -= 1
            c -= 1
        # diff = b - a + (c - a)
        # if diff >= 2:
        #     a += 1
        return min(a, b, c)


# 作者：milestian
# 链接：https://www.nowcoder.com/discuss/500267?type=all&order=time&pos=&page=1&channel=1009&source_id=search_all
# 来源：牛客网
"""
用三个不同的值换礼物
如： 2,4,4 换取的最大礼物为3
"""


class Solution1:
    def numberofprize(self, a, b, c):
        l = [a, b, c]
        minN = min(l)
        l = [x - minN for x in l]
        count = sum(l)
        result = minN
        # 二分
        left = 0
        right = max(l)
        while left < right:
            x = (left + right) // 2
            need = 0
            for y in l:
                if y >= x:
                    need += x
                else:
                    need += 2 * (x - y)
            if need > count:
                right = x
            else:
                left = x + 1

        return minN + left - 1

    def numberofprize1(self, a, b, c):
        arr = [a, b, c]
        arr.sort()
        minE = min(arr)
        maxE = max(arr)
        left = minE
        right = maxE
        while left <= right:
            mid = left + (right - left) // 2
            pos = 0
            disPos = 0
            for i in range(3):
                if arr[i] > mid:
                    pos += arr[i] - mid
                else:
                    disPos += mid - arr[i]
            if pos > 2 * disPos:
                left = mid + 1
            elif pos < 2 * disPos:
                right = mid - 1
            else:
                return mid
        return left - 1


if __name__ == '__main__':
    # arr = list(map(int, input().strip().split(",")))
    # arr.sort()
    # # print(arr)
    # # print(arr)
    # solution = Solution()
    # res = solution.numberofprize(arr[0], arr[1], arr[2])
    # print(res)
    # sol1 = Solution1()
    # print(sol1.numberofprize(1, 9, 10))
    # print(sol1.numberofprize1(1, 9, 10))
    # print(sol1.numberofprize(1000000000, 1000000000, 0))
    # print(sol1.numberofprize1(1000000000, 1000000000, 0))
    pass

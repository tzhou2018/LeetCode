'''
@Time    : 2020/2/8 20:36
@FileName: 03findMedianSortedArrays.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''

# 控制时间复杂度为 log(m+n) 有点不容易，先按常规方法;
# 优化解法参加：https://mp.weixin.qq.com/s/FBlH7o-ssj_iMEPLcvsY2w
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        p, q = 0, 0
        # 获取中位数的索引
        mid = ((m + n) // 2 - 1, (m + n) // 2) if (m + n) % 2 == 0 \
            else ((m + n) // 2, (m + n) // 2)
        all = []
        while p < m and q < n:
            if nums1[p] <= nums2[q]:
                all.append(nums1[p])
                p += 1
            else:
                all.append(nums2[q])
                q += 1
        if p >= m:
            while q < n:
                all.append(nums2[q])
                q += 1
        else:
            while p < m:
                all.append(nums1[p])
                p += 1
        ret = (all[mid[0]] + all[mid[1]]) / 2.0
        return ret


def findMedianSortedArrays(num1, num2):
    num1.extend(num2)
    num1.sort()
    lenNum1 = len(num1)
    return (num1[lenNum1 // 2] + num1[lenNum1 // 2 - 1]) / 2.0 if lenNum1 & 1 == 0 \
        else num1[lenNum1 // 2]


if __name__ == '__main__':
    print(findMedianSortedArrays([1, 2], [3, 4]))

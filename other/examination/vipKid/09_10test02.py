"""
@Time       : 2020/9/10 19:48
@FileName   : 09_10test02.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""
"""
编写一个算法把中文的字符串转换成整数，不用考虑long的溢出问题，假设它可以存储任意大的整数。 
long parseChineseNumber(string s); 测试用例： 
1. "一千零一" -> 1001 
2. "一千零一万五千四百三十二亿九千八百七十六万四千三百零二" -> 1001543298764302 
3. "十五" -> 15 4. "五万三" -> 53000 
5. "四万亿" -> 4000000000000
"""

def test01():
    dict = {"亿": 100000000, "万": 10000, "千": 1000, "百": 100, "十": 10,
            "九": 9, "八": 8, "七": 7, "六": 6, "五": 5, "四": 4, "三": 3, "二": 2, "一": 1, "零": 1}
    arr = input().strip()
    res = 0
    # for i in range(len(arr)):
    #     res += dict[arr[i]] * arr[i]
    start = 0
    yiList = ["亿", "万", "千", "百", "十", "零"]
    temp = 0

    while start < len(arr):
        # if arr[start] == "零":
        #     start += 1
        #     continue
        if arr[start] not in yiList:
            temp = dict[arr[start]]
            if start == len(arr) - 1:
                res += dict[arr[start]] * temp

            # start += 1
        if arr[start] in yiList:
            res += dict[arr[start]] * temp
        start += 1
    print(res)
    pass


def test02(arr):
    res = 1
    if "万" in arr:
        pass


if __name__ == '__main__':
    test01()

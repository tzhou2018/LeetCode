"""
@Time       : 2020/9/8 20:19
@FileName   : 09_08test02.py
@Author     : Solarzhou
@Email      : t-zhou@foxmail.com
"""
"""
携程第二题：
给出字符，求字符组合的路径；
若存在循环路径，标出。
例子：
输入：
a bc d eag f
输出：
abdef
abdaf--circular dependency
abdgf
acdef
acdaf--circular dependency
acdgf
原题：
https://www.nowcoder.com/discuss/503503?type=post&order=time&pos=&page=1&channel=1009&source_id=search_post
"""


def test023():
    arr = input().strip().split(" ")
    arr = list(arr)
    n = len(arr)
    res = []
    temp = []
    # 记录那些字符串存在循环
    flag = []
    map = {}

    def recursive(cur, f):
        # recursion terminator
        if cur == n:
            res.append("".join(temp))
            flag.append(f)
            return
        # 取当前的字符串开始做判断
        # precess logic in current level
        str1 = arr[cur]
        for i in range(len(str1)):
            char = str1[i]
            tf = f
            c = map.get(char)
            if c != None and c > 0:
                tf = False
            map[char] = c + 1 if c != None else 1
            temp.append(str1[i])
            # drill down
            recursive(cur + 1, tf)
            # reverse the current level status if needed
            map[char] = c
            temp.pop(len(temp) - 1)
        pass

    recursive(0, True)
    for e in res:
        print(e, end="")
        if not flag[0]:
            print("--circular dependency")
        else:
            print()
        flag.pop(0)


if __name__ == '__main__':
    # a = ["a", "b"]
    # for index, k in enumerate(a):
    #     print(index, k)
    test023()

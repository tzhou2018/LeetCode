'''
@Time    : 2020/4/23 14:22
@FileName: 5.6test01.py
@Author  : Solarzhou
@Email   : t-zhou@foxmail.com
'''
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)
"""
读取多行数据
"""
import sys

try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        print(int(lines[0]) + int(lines[1]))
except:
    pass

# python3
import sys

for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))
# 样例数据
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

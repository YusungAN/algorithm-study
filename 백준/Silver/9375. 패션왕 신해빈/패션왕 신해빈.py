import sys
from collections import defaultdict

input = sys.stdin.readline
T = int(input())
res = []
for i in range(T):
    n = int(input())
    if n == 0:
        res.append(0)
        continue
    dic = defaultdict(list)
    c_li = []
    _sum = 1
    for j in range(n):
        a, b = input().split()
        dic[b].append(a)
        c_li.append(b)
    c_li = list(set(c_li))
    for j in c_li:
        _sum *= len(dic[j])+1

    res.append(_sum-1)

for i in res:
    print(i)

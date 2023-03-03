import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
dic = {}
ins = []
for _ in range(n):
    s, k = input().rstrip().split(' ')
    k = int(k)
    dic[k] = 0
    ins.append((s, k))

for s, k in ins:
    if s == 'G':
        for i in dic:
            if i >= k:
                dic[i] += 1
    else:
        for i in dic:
            if i <= k:
                dic[i] += 1

_max = 0
for i in dic:
    if _max < dic[i]:
        _max = dic[i]
print(n-_max)


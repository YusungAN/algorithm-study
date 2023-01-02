import sys
from collections import defaultdict

dic = defaultdict(int)
n, m = map(int, sys.stdin.readline().rstrip().split(' '))

for i in range(n):
    dic[sys.stdin.readline().rstrip()] = 1

res = []
for i in range(m):
    temp = sys.stdin.readline().rstrip()
    if dic[temp] == 1:
        res.append(temp)

print(len(res))
res.sort()
for i in res:
    print(i)
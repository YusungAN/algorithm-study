import sys
from collections import defaultdict

dic = defaultdict(int)

n, m = map(int, sys.stdin.readline().split(' '))
li = []
res = []
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    dic[temp] = i+1
    li.append(temp)


for i in range(m):
    temp = sys.stdin.readline().rstrip()
    if temp.isdigit():
        res.append(li[int(temp)-1])
    else:
        res.append(dic[temp])

for i in res:
    print(i)

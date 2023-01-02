import sys
from collections import defaultdict

dic = defaultdict(int)

n, m = map(int, sys.stdin.readline().split(' '))
li = []
for i in range(n):
    dic[sys.stdin.readline().rstrip()] = 1
for i in range(m):
    li.append(sys.stdin.readline().rstrip())

sum = 0
for i in li:
    sum += dic[i]

print(sum)
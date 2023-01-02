import sys
from math import gcd, sqrt

n = int(sys.stdin.readline().rstrip())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline().rstrip()))
li.sort()
sub_li = []
for i in range(n-1):
    sub_li.append(li[i+1]-li[i])

gcd_n = sub_li[0]
for i in range(1, len(sub_li)):
    gcd_n = gcd(gcd_n, sub_li[i])

res = []
res.append(gcd_n)

for i in range(2, int(sqrt(gcd_n))+1):
    if gcd_n % i == 0:
        res.append(i)
        res.append(gcd_n // i)

res = list(set(res))
res.sort()
for i in res:
    print(i, end=' ')
import sys

n, k = map(int, sys.stdin.readline().rstrip().split(' '))

res = 1
for i in range(k):
    res *= n
    n -= 1

fac = 1
for i in range(k-1):
    fac *= k
    k -= 1

print((res//fac)%10007)
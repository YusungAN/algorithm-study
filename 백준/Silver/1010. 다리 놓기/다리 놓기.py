import sys

N = int(sys.stdin.readline().rstrip())

def com(n, k):
    res = 1
    for i in range(k):
        res *= n
        n -= 1

    fac = 1
    for i in range(k-1):
        fac *= k
        k -= 1

    return res//fac
res = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split(' '))
    res.append(com(b, a))

for i in res:
    print(i)
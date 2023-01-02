import sys

input = sys.stdin.readline

def sum(n):
    res = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            res += n//i
        else:
            res -= n//i
    return res

s, t = map(int, input().split(' '))
print(sum(t)-sum(s-1) if s > 1 else sum(t))
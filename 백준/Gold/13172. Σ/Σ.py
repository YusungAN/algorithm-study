import sys
from math import gcd
input = sys.stdin.readline

p = 10**9+7
res = 0

def pow(a, b, c):
    if b == 1:
        return a%c
    tmp = pow(a, b // 2, c)
    if b % 2 == 1:
        return (tmp*tmp*a) % c

    return (tmp*tmp) % c


for _ in range(int(input())):
    n, s = map(int, input().split(' '))
    g = gcd(n, s)
    n //= g
    s //= g
    res = (res + s*pow(n, p-2, p) % p) % p

print(res)

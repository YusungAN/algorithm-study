import sys

input = sys.stdin.readline

p = 10**9+7
fac = [1]*600001

for i in range(1, 600001):
    fac[i] = (fac[i-1]*i) % p


def pow(a, b, c):
    if b == 1:
        return a % c
    tmp = pow(a, b // 2, c)
    if b % 2 == 1:
        return (tmp*tmp*a) % c

    return (tmp*tmp) % c


res = 1
for i in range(int(input())):
    a, b = map(int, input().split(' '))
    _min = min(a, b)

    top = fac[a+b]
    bot = fac[_min]*fac[a+b-_min] % p
    com = top*pow(bot, p-2, p) % p - 1
    res = res*com % p

print(res % p)

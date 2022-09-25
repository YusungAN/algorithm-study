import sys

input = sys.stdin.readline

p = 1000000007
fac = [0]*4000001
fac[0] = 1
for i in range(1, 4000001):
    fac[i] = fac[i-1]*i % p

def com(n, k):
    def pow(a, b, c):
        if b == 1:
            return a%c
        tmp = pow(a, b // 2, c)
        if b % 2 == 1:
            return (tmp*tmp*a) % c

        return (tmp*tmp) % c

    top = fac[n]
    bot = fac[k]*fac[n-k]
    print(top*pow(bot, p-2, p) % p)

for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    com(n, k)
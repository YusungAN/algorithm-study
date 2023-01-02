import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))
p = 1000000007

# def factorial1(N):
#     n = 1
#     for i in range(2, N+1):
#         n *= i % p
#     return n

def fac(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % p
    return n

def pow(a, b, c):
    if b == 1:
        return a%c
    tmp = pow(a, b // 2, c)
    if b % 2 == 1:
        return (tmp*tmp*a) % c

    return (tmp*tmp) % c

top = fac(n)
bot = fac(k)*fac(n-k)
print(top*pow(bot, p-2, p)%p)
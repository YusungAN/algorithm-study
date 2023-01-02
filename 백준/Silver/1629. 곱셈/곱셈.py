import sys

input = sys.stdin.readline

a, b, c = map(int, input().split(' '))

def pow(a, b, c):
    if b == 1:
        return a%c
    tmp = pow(a, b // 2, c)
    if b % 2 == 1:
        return (tmp*tmp*a)%c

    return (tmp*tmp)%c

print(pow(a%c, b, c))
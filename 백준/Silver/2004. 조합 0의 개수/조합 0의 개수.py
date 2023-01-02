import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))


def two_count_fac(n):
    cnt = 0
    while n > 0:
        n //= 2
        cnt += n
    return cnt

def five_count_fac(n):
    cnt = 0
    while n > 0:
        n //= 5
        cnt += n
    return cnt

print(min(five_count_fac(n)-five_count_fac(n-k)-five_count_fac(k), two_count_fac(n)-two_count_fac(n-k)-two_count_fac(k)))
import sys


input = sys.stdin.readline

n = int(input())
arr = [0]*10
arr[0] += 1


def calc(n):
    a = [0]*10
    while n > 0:
        a[n % 10] += 1
        n //= 10
    return a

mull = 1
while n > 0:
    while n % 10 != 9:
        n += 1
        a = calc(n)
        # print(a)
        for i in range(10):
            arr[i] -= a[i]*mull

    tmp = n // 10 + 1
    for i in range(10):
        arr[i] += tmp*mull
    arr[0] -= 1*mull

    n //= 10
    mull *= 10

arr[0] -= 1

print(*arr)
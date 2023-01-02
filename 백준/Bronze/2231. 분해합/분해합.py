import sys

N = int(sys.stdin.readline().rstrip())


def func(n):
    for i in range(n):
        ii = i
        sum = i
        while i > 0:
            sum += i % 10
            i //= 10
        if sum == n:
            print(ii)
            return
    print('0')


func(N)

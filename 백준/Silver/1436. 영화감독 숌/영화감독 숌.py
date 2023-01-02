import sys

n = int(sys.stdin.readline().rstrip())

cnt = 1
start = 666


def func6(num):
    stack = 0
    while num > 0:
        if num % 10 == 6:
            stack += 1
        else:
            stack = 0
        num //= 10
        if stack >= 3:
            return True
    return False


while True:
    if cnt == n:
        print(start)
        break
    start += 1
    if func6(start):
        cnt += 1

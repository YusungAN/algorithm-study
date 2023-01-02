import sys


input = sys.stdin.readline
T = int(input())

fac = 1
for i in range(2, T+1):
    fac *= i

cnt = 0
while fac % 10 == 0:
    cnt += 1
    fac //= 10

print(cnt)

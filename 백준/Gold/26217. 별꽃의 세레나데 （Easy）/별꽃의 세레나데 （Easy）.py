import sys

input = sys.stdin.readline

res = 1
N = int(input())
for i in range(N-1, 0, -1):
    res += N/(N-i)

print(res)
import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split(' ')))
dp = [[0]*n for _ in range(n)]

for size in range(1, n+1):
    for start in range(n):
        end = start + size - 1
        if end >= n:
            break

        if size == 1:
            dp[start][end] = 1
            continue

        if li[start] == li[end] and dp[start+1][end-1] == 1:
            dp[start][end] = 1
            continue
        if li[start] == li[end] and end - start == 1:
            dp[start][end] = 1
        # print(dp)

for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    print(dp[a-1][b-1])
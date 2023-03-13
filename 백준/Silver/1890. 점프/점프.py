import sys

input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split(' '))) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        if dp[i][j] != 0:
            if 0 <= i+li[i][j] < n:
                dp[i+li[i][j]][j] += dp[i][j]
            if 0 <= j + li[i][j] < n:
                dp[i][j+li[i][j]] += dp[i][j]

print(dp[-1][-1])


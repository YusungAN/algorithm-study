import sys

input = sys.stdin.readline
n, k = map(int, input().split(' '))
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][1] = 1

for j in range(2, k+1):
    for i in range(n+1):
        for kk in range(i+1):
            dp[i][j] = (dp[i][j]+dp[kk][j-1]) % 1000000000

print(dp[n][k])

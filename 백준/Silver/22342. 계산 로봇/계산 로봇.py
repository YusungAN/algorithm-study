import sys

input = sys.stdin.readline

m, n = map(int, input().split(' '))
li = [list(map(int, list(input().rstrip()))) for _ in range(m)]
dp = [[0]*n for _ in range(m)]

_max = 0
for i in range(m):
    dp[i][0] = li[i][0]

for i in range(1, n):
    for j in range(m):
        dp[j][i] = max(0 if j == 0 else dp[j-1][i-1], dp[j][i-1], 0 if j == m-1 else dp[j+1][i-1])
        _max = max(_max, dp[j][i])
        dp[j][i] += li[j][i]

print(_max)
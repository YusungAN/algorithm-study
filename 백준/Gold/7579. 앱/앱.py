import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost_sum = sum(cost)

dp = [[0]*(cost_sum+1) for _ in range(n)]

for i in range(n):
    for j in range(cost_sum+1):
        if j - cost[i] >= 0:
            dp[i][j] = max(dp[i-1][j-cost[i]]+mem[i], dp[i][j])
        dp[i][j] = max(dp[i][j], dp[i-1][j])


for i in range(cost_sum+1):
    if dp[n-1][i] >= m:
        print(i)
        break
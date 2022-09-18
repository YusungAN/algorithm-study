import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))
mems = list(map(int, input().split(' ')))
costs = list(map(int, input().split(' ')))
max_cost = sum(costs)
dp = [[0]*(max_cost+1) for _ in range(n+1)]
res = max_cost

for i in range(1, n+1):
    for j in range(1, max_cost+1):
        if j < costs[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(mems[i-1]+dp[i-1][j-costs[i-1]], dp[i-1][j])

        if dp[i][j] >= m:
            res = min(res, j)

print(res)

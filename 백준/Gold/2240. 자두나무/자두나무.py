import sys

input = sys.stdin.readline

T, W = map(int, input().split())

dp = [[0]*(W+1) for _ in range(T+1)]

for i in range(1, T+1):
    tree_i = int(input())

    for j in range(W+1):
        now = j % 2 + 1
        if now == tree_i:
            dp[i][j] = dp[i-1][j]+1
        else:
            if j > 0:
                dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]


# print(dp)
print(dp[T][W])

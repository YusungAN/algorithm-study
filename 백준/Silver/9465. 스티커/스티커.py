import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [[0]*n for _ in range(2)]
    li = [list(map(int, input().split(' '))) for _ in range(2)]
    dp[0][0] = li[0][0]
    dp[1][0] = li[1][0]
    ans = max(dp[0][0], dp[1][0])
    if n > 1:
        dp[0][1] = li[0][1]+li[1][0]
        dp[1][1] = li[1][1]+li[0][0]
        ans = max(ans, dp[0][1], dp[1][1])
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1]+li[0][i], dp[0][i-2]+li[0][i], dp[1][i-2]+li[0][i])
        dp[1][i] = max(dp[0][i-1]+li[1][i], dp[1][i-2]+li[1][i], dp[0][i-2]+li[1][i])
        ans = max(ans, max(dp[0][i], dp[1][i]))
    print(ans)
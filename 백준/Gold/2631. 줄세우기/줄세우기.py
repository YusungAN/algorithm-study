import sys

input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]

dp = [1]*n
for i in range(0, n):
    for j in range(0, i):
        if li[j] < li[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
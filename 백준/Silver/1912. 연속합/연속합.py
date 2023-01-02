import sys

input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split(' ')))

dp = [0]*n

dp[0] = v[0]
for i in range(1, n):
    dp[i] = max(v[i], v[i]+dp[i-1])

print(max(dp))
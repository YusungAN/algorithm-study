import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

_max = 0
dp = [0]*(n+1)
for i in li:
    dp[i] = dp[i-1]+1
    _max = max(dp[i], _max)
print(n-_max)
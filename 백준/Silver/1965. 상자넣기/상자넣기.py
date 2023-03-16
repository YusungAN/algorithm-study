import sys

input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split(' ')))
dp = [0]*n
dp[0] = 1
for i in range(1, n):
    _max = 0
    for j in range(0, i):
        if li[j] < li[i]:
            _max = max(_max, dp[j])
    dp[i] = _max+1

print(max(dp))
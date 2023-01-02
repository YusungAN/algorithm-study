import sys

input = sys.stdin.readline

n = int(input())
v = []
for i in range(n):
    v.append(int(input()))

dp = []
dp.append(v[0])
if len(v) > 1:
    dp.append(v[0]+v[1])
if len(v) > 2:
    dp.append(max(v[0]+v[2], v[1]+v[2]))

for i in range(3, n):
    dp.append(max(v[i]+dp[i-2], v[i]+v[i-1]+dp[i-3]))


print(dp[n-1])
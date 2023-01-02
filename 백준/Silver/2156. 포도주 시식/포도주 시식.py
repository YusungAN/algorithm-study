import sys

input = sys.stdin.readline

n = int(input())
v = []
for _ in range(n):
    v.append(int(input()))

dp = [v[0]]
if len(v) >= 2:
    dp.append((v[0]+v[1]))
if len(v) >= 3:
    dp.append(max(v[0]+v[2], v[1]+v[2], v[0]+v[1]))

for i in range(3, n):
    dp.append(max(v[i]+dp[i-2], v[i]+v[i-1]+dp[i-3], dp[i-1]))

print(max(dp))

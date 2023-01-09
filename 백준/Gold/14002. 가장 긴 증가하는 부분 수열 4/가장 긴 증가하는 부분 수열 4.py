import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split(' ')))

dp = [1]*(n)

for i in range(n):
    for j in range(i):
        if li[j] < li[i]:
            dp[i] = max(dp[i], dp[j]+1)

ans = max(dp)
print(ans)
res = []
for i in range(n-1, -1, -1):
    if dp[i] == ans:
        res.append(li[i])
        ans -= 1
print(*reversed(res))
import sys

input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split(' ')))

dp = [1]*n
for i in range(1, n):
    dp2 = [1]
    for j in range(0, i):
        if v[j] < v[i]:
            dp2.append(dp[j]+1)
    dp[i] = max(dp2)



print(max(dp))

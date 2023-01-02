import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))
w = []
v = []
for i in range(n):
    a, b = map(int, input().split(' '))
    w.append(a)
    v.append(b)

dp = [[0]*(k+1) for i in range(n)]

for i in range(n):
    for j in range(k+1):
        if i == 0 and w[i] <= j:
            dp[i][j] = v[i]
        elif w[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])

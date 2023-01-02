import sys

input = sys.stdin.readline

n = int(input())
v = []
for i in range(n):
    v.append(tuple(map(int, input().split(' '))))

v.sort()
vv = []
for i in v:
    vv.append(i[1])

dp = [1]*n
for i in range(1, n):
    dp2 = [1]
    for j in range(0, i):
        if vv[j] < vv[i]:
            dp2.append(dp[j]+1)
    dp[i] = max(dp2)

print(n-max(dp))

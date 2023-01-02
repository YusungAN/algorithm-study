import sys

input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split(' ')))
down_v = list(reversed(v))
up_dp = [1]*n
down_dp = [1]*n
dp = [1]*n
for i in range(1, n):
    up_dp2 = [1]
    down_dp2 = [1]
    for j in range(0, i):
        if v[j] < v[i]:
            up_dp2.append(up_dp[j]+1)
        if down_v[j] < down_v[i]:
            down_dp2.append(down_dp[j]+1)
    up_dp[i] = max(up_dp2)
    down_dp[i] = max(down_dp2)

down_dp.reverse()
for i in range(n):
    dp[i] = up_dp[i]+down_dp[i]

print(max(dp)-1)
import sys

input = sys.stdin.readline

n = int(input())
dp = [0]*30
dp[1] = 3
for i in range(n):
    if i >= 3 and i % 2 == 1:
        dp[i] += 2
    if i-2 >= 0 and dp[i-2] != 0:
        dp[i] += dp[i-2]*3
    tmp = i-4
    while tmp >= 0:
        dp[i] += dp[tmp]*2
        tmp -= 2

print(dp[n-1])
import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))
li = []
for i in range(n):
    li.append(int(input()))

dp = [1]+[0]*k

for i in li:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[-1])
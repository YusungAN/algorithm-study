import sys

input = sys.stdin.readline


k = int(input())
li = []
for i in range(k):
    li.append(tuple(map(int, input().split(' '))))

dp = [[0]*k for _ in range(k)]

for size in range(1, k):
    for start in range(k):
        end = size + start
        if end >= len(li):
            break

        res = float("inf")
        for k in range(start, end):
            res = min(res, dp[start][k]+dp[k+1][end]+li[start][0]*li[k][1]*li[end][1])

        dp[start][end] = res

print(dp[0][-1])

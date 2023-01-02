import sys

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    li = list(map(int, input().split(' ')))

    sums = [0]*(k+1)
    for i in range(1, k+1):
        sums[i] = sums[i-1]+li[i-1]
    dp = [[0]*k for _ in range(k)]

    for i in range(1, k):
        for j in range(k):
            if i+j >= len(li):
                break

            res = float("inf")
            for k in range(j, j+i):
                res = min(res, dp[j][k]+dp[k+1][j+i]+sums[i+j+1]-sums[j])

            dp[j][i+j] = res

    print(dp[0][-1])

import sys

input = sys.stdin.readline

N = int(input())
v = []
for i in range(N):
    v.append(list(map(int, input().split(' '))))

dp = [[0, 0, 0] for _ in range(N)]
ans = []
for i in range(3):
    dp[0][i] = v[0][i]
    dp[0][(i+1) % 3] = 1000**2+1
    dp[0][(i+2) % 3] = 1000**2+1

    for j in range(1, N-1):
        dp[j][0] = min(v[j][0]+dp[j-1][1], v[j][0]+dp[j-1][2])
        dp[j][1] = min(v[j][1]+dp[j - 1][0], v[j][1]+dp[j - 1][2])
        dp[j][2] = min(v[j][2]+dp[j - 1][0], v[j][2]+dp[j - 1][1])

    ans.append(min(v[N-1][(i+2) % 3]+dp[N-2][(i+1) % 3],
                   v[N-1][(i+1) % 3]+dp[N-2][i],
                   v[N-1][(i+2) % 3]+dp[N-2][i],
                   v[N-1][(i+1) % 3]+dp[N-2][(i+2) % 3]))

print(min(ans))

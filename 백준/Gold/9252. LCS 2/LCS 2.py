import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

a = len(s1)
b = len(s2)

dp = [[0 for _ in range(b+1)] for _ in range(a+1)]

res = []
for i in range(1, a+1):
    for j in range(1, b+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
res = []
na, nb = a, b
while len(res) < dp[-1][-1]:
    if dp[na-1][nb] == dp[na][nb]:
        na -= 1
    elif dp[na][nb-1] == dp[na][nb]:
        nb -= 1
    else:
        res.append(s1[na-1])
        na -= 1
        nb -= 1

print(''.join(reversed(res)))

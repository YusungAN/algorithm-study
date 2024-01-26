import sys

input = sys.stdin.readline

n = int(input())

T = []
P = []
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0]*n

for i in range(n-1, -1, -1):
    dp[i] = max((P[i] if i+T[i] <= n else 0)+(dp[i+T[i]] if i+T[i] < n else 0), dp[i+1] if i < n-1 else 0)

# print(T)
# print(P)
# print(dp)
print(dp[0])

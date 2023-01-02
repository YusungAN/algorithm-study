import sys

input = sys.stdin.readline

N = int(input())
s = input().rstrip()

dp = [0]+[float('inf')]*(N-1)
for i in range(1, N):
    prev = ''
    if s[i] == 'B':
        prev = 'J'
    elif s[i] == 'O':
        prev = 'B'
    else:
        prev = 'O'
    for j in range(0, i):
        if s[j] == prev:
            dp[i] = min(dp[j]+(i-j)**2, dp[i])

print(dp[-1] if dp[-1] != float('inf') else -1)
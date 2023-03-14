import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp0 = [0]*(n+3)
    dp1 = [0] * (n + 3)
    dp0[0] = 1
    dp1[0] = 0
    dp0[1] = 0
    dp1[1] = 1
    for i in range(2, n+1):
        dp0[i] = dp0[i-1]+dp0[i-2]
        dp1[i] = dp1[i - 1] + dp1[i - 2]
    print(dp0[n], dp1[n])

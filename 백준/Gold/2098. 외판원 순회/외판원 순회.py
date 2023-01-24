import sys

input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (1 << n) for _ in range(n)]


def tsp(node, visited):
    if visited == (1 << n) - 1:
        if w[node][0] == 0:
            return float('inf')
        else:
            return w[node][0]

    if dp[node][visited] != -1:
        return dp[node][visited]

    dist = float('inf')
    for i in range(1, n):
        if visited & 1 << i == 0 and w[node][i] != 0:
            dist = min(dist, tsp(i, visited | 1 << i) + w[node][i])

    dp[node][visited] = dist
    return dp[node][visited]


print(tsp(0, 1))

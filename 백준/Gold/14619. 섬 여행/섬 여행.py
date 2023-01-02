import sys
from collections import defaultdict

input = sys.stdin.readline

graph = defaultdict(list)

N, M = map(int, input().split(' '))
h_li = list(map(int, input().split(' ')))
for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)


dp = [[-1]*501 for _ in range(101)]


def findh(a, k):
    if dp[a][k] != -1:
        return dp[a][k]
    if k == 0:
        return h_li[a-1]
    dp[a][k] = float('inf')
    for i in graph[a]:
        dp[a][k] = min(dp[a][k], findh(i, k-1))
    if dp[a][k] == float('inf'):
        dp[a][k] = -1
    return dp[a][k]


for _ in range(int(input())):
    a, k = map(int, input().split(' '))
    print(findh(a, k))
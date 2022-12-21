import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


for _ in range(int(input())):
    v, e = map(int, input().split(' '))
    graph = [[] for _ in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split(' '))
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (v + 1)


    def dfs(start, now):
        # print(start, now)
        for i in graph[start]:
            if visited[i] == 0:
                visited[i] = -1*now
                res = dfs(i, -1 * now)
                if not res:
                    return False
            elif visited[i] == now:
                return False
        return True


    for j in range(1, v + 1):
        if visited[j] == 0:
            visited[j] = 1
            if not dfs(j, 1):
                print('NO')
                break
    else:
        print('YES')
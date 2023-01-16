import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**5)

case_idx = 0
while True:
    case_idx += 1
    n, m = map(int, input().split(' '))
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split(' '))
        graph[a].append(b)
        graph[b].append(a)

    visited = [False]*(n+1)
    cnt = 0

    def dfs(prev, now):
        visited[now] = True
        flag = True
        for i in graph[now]:
            if i != prev and visited[i]:
                return False
            elif not visited[i]:
                flag = flag and dfs(now, i)

        return flag

    for i in range(1, n+1):
        if not visited[i]:
            res = dfs(0, i)
            if res:
                cnt += 1
    if cnt == 0:
        print('Case {}: No trees.'.format(case_idx))
    elif cnt == 1:
        print('Case {}: There is one tree.'.format(case_idx))
    else:
        print('Case {}: A forest of {} trees.'.format(case_idx, cnt))